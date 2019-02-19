function [packet_data,unprocessed_data] = parse_serial_data(data_array)
	% Function for parsing incoming packets into CHR packets.  During each
	% call, this function will parse up to one packet, leaving the remaining
	% data in the return array 'unprocessed_data'.

	MINIMUM_PACKET_LENGTH = 7;
	
	packet_data.Address = 0;
	packet_data.PT = 0;
	packet_data.Length = 0;
	packet_data.NewPacket = 0;
	packet_data.Checksum = 0;
	packet_data.BadChecksum = 0;
	packet_data.data = [];
	
	unprocessed_data = [];
	
	% Search for preambles
	packet_index = [];
	data_length = length(data_array);
	for index=1:(data_length-2)
		if (data_array(index) == 's') && (data_array(index+1) == 'n') && (data_array(index+2) == 'p')
			packet_index = index;
			break;
		end
	end
	
	if isempty(packet_index)
		% No packet preamble was found in the data.  Discard data and exit. 
		% (We discard the data because without a preamble, we can't possibly
		% use the data, even if it happened to be a part of a real packet -
		% we missed the beginning, so it is useless data now).
		return;
	end

	% If found at least one preamble, parse it and extract packet
	% contents

	% Check to make sure that there is enough data left in the
	% received data to contain the entire contents of this
	% packet.  If not, we should wait to receive the rest
	if (data_length - packet_index) >= (MINIMUM_PACKET_LENGTH - 1)
		% Extract the packet header and compute the full packet
		% size.  Return if not enough data for the full packet.
		PT = data_array(packet_index + 3);
		Address = data_array(packet_index + 4);

		% Check to see if this packet has data
		if bitand(PT,bitshift(1,7))
			% Packet has data.  Check to see if it is a batch
			% operation
			if bitand(PT,bitshift(1,6))
				% Batch operation.
				BatchSize = bitand(bitshift(PT,-2),15); % Extract lower-order four bits
				Length = 7 + BatchSize*4;
			else
				% This packet has data, but it is not a batch
				% operation.  Packet size is 11.
				Length = 11;
			end
		else
			% This packet has no data.  Packet size is 7
			Length = 7;
		end

		packet_data.PT = PT;
		packet_data.Address = Address;
		packet_data.Length = Length;

		% Now we have the packet length.  Check to make sure
		% there is enough data from the serial port to construct the
		% full packet.  If not, save the incomplete data and
		% return for next time.
		if (data_length - packet_index) < (Length-1)
			unprocessed_data = data_array(packet_index:end);
			return;
		end

		% Check to make sure that the checksum is valid
		computed_checksum = sum( uint16( data_array(packet_index:(packet_index+Length-3)) ) );
		received_checksum = typecast(flipud(uint8(data_array((packet_index+Length-2):(packet_index+Length-1)))), 'uint16' );

		if computed_checksum ~= received_checksum
			packet_data.Checksum = computed_checksum;
			packet_data.BadChecksum = 1;

			% If there is more stuff available, copy it to the
			% unprocessed data output and return
			if (packet_index+Length) <= length(data_array)
				unprocessed_data = data_array((packet_index+Length):end);
			end

			return;
		end

		% If we got here, we've received a good packet!  Copy the
		% packet data to the output, set the flag indicating a good
		% packet was received, and leave.
		if Length > MINIMUM_PACKET_LENGTH		% Of course, only copy out the data if the packet had some...
			packet_data.data = data_array((packet_index + 5):(packet_index + Length - 3));
		end

		packet_data.NewPacket = 1;

		% If there is extra stuff available, copy it out
		if (packet_index+Length) <= length(data_array)
			unprocessed_data = data_array((packet_index+Length):end);
		end

		% Done!
		return;
	else
		% If we found a start sequence but there isn't enough data to form a full packet,
		% then copy the unused data to the output and leave.
		unprocessed_data = data_array(packet_index:end);
		return;
	end
end
