% cleanup.m  This closes all serial ports and handles other housekeeping
% issues on shutdown
function [] = cleanup()
    
	% Close all ports
	ports = instrfind;
    if ~isempty(ports)
		fclose(ports);
	end
	
	% Stop and delete all timers
	timers = timerfindall();
	if ~isempty(timers)
		stop(timers);
		delete(timers);
	end
	
end
