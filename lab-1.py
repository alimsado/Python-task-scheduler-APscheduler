from telnetlib import Telnet
import datetime

# cmd_exec = input('Enter the Command : ')
# Define the log file path
log_file_path = 'log-running-task.txt'

# Open a file for appending log entries
with open(log_file_path, 'a') as log_file:
    # Add a timestamp to the log
    current_time = datetime.datetime.now()
    log_file.write(f'Task executed at {current_time}\n')

# Open a file for writing the output
with open('telnet_output.txt', 'w') as output_file:
    mytel = Telnet('192.168.1.13')
    mytel.write(b'admin\n')
    mytel.write(b'admin\n')
    mytel.write(b'terminal length 0\n')
    # mytel.write(cmd_exec.encode('ascii') + b'\n')
    mytel.write(b'sh ip int brief\n')
    mytel.write(b'exit\n')
    # Read the Telnet output and write it to the file
    output = mytel.read_all()
    output_file.write(output.decode('ascii'))

