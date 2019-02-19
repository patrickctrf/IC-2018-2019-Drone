function DUT_callback(obj, event, DUT_port)
% Callback function for handling serial communication with DUT in gimballed
% temperature chamber
%
% Reads all available data and passes it to data structures
%
%


% Create persistent variable for storing previous data collects
persistent stored_data;

if isempty(stored_data)
    stored_data = [];
end

% If port is open, check to see if new data is available.  If so, read it
% in and do stuff with it
if ~strcmp(DUT_port.status,'open')
	return;
end

if ~DUT_port.BytesAvailable
	return;
end

       
% New data is available.  Read it in!
try
	new_data = fread(DUT_port,DUT_port.BytesAvailable);
catch exception
	fprintf('ERROR: Failed to read from DUT port.  Shutting down.\n');
	cleanup();
	return;
end

data_array = [stored_data;new_data];

% Go through the data and keep parsing it as long as there are new
% packets available.  The 'parse_serial_data' only parses a single packet
% at a time.
packet.NewPacket = 1;
while packet.NewPacket == 1
	[packet,data_array] = parse_serial_data(data_array);
	
	% Report bad checksum if appropriate
	if packet.BadChecksum
% 		fprintf('ERROR: Bad Checksum.\n');
	end
	
	% If packet was received, do stuff with it
	if packet.NewPacket == 1
		% HANDLE RAW GYRO DATA PACKET
		if packet.Address == 86
			% Extract the gyro data
			gyro_x = typecast( flipud(uint8(packet.data(1:2))), 'int16' );
			gyro_y = typecast( flipud(uint8(packet.data(3:4))), 'int16' );
			gyro_z = typecast( flipud(uint8(packet.data(5:6))), 'int16' );

			got_gyro_data = 1;
% 			fprintf('%d\t%d\t%d\n',gyro_x,gyro_y,gyro_z);
		end 

		% HANDLE TEMPERATURE DATA PACKET
		if packet.Address == 118
			temperature = typecast( flipud(uint8(packet.data(1:4))), 'single' );
			got_temperature_data = 1;
% 			fprintf('%3.2f\n',temperature);
		end

		% If we received gyro and temperature data, log it to
		% the workspace if logging is enabled.
		if got_temperature_data && got_gyro_data
			got_temperature_data = 0;
			got_gyro_data = 0;

			if GDATA.logging_data == 1 && GDATA.selected_DUT > 0
				if GDATA.DUT_samples_collected < GDATA.MAX_SAMPLES
					GDATA.DUT_samples_collected = GDATA.DUT_samples_collected + 1;
					GDATA.DUT_data(GDATA.DUT_samples_collected,:) = [single([GDATA.selected_DUT,gyro_x,gyro_y,gyro_z]),temperature];
				else
					fprintf('Maximum datapoints were collected.  Logging disabled.\n');
					GDATA.logging_data = 0;
				end
			end
		end

	end

end % End of "while new packet found"

% Copy whatever is left in the data array to our local persistent
% variable so that we can use it next time we go through the array.
stored_data = data_array;

% We are done here!
