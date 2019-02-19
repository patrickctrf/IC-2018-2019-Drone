% Initializes serial port objects and assigns message handlers

% Before running, run cleanup function to close ports and remove timers
% that may have been running before.
cleanup();

% Clear workspace and close any open figures
close all;
clear all;

port_string = 'COM1';

% Create serial port objects
device_port = serial(port_string,'BaudRate',115200,'DataBits',8,'Parity','None');

% Attempt to open serial ports
device_opened = 1;
try
    % Create callback function.
    device_port.BytesAvailableFcnMode = 'byte';
    device_port.BytesAvailableFcnCount = 7;
    device_port.BytesAvailableFcn = {@DUT_callback,device_port};
    
    fopen(device_port);
catch ME
    device_opened = 0;
    fprintf(1,'ERROR: Failed to open DUT port.  Is the port already open?\n');
end

% If we failed to open any of the individual ports, quit
if (device_opened == 0)
    cleanup();
end

% Get rid of variables that we aren't using anymore
clear('DUT_board_opened','DUT_opened','control_port_opened','DUT_control_timer_period');

