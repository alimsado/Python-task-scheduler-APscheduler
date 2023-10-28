# Telnet Automation Script

This Python script is designed to automate tasks over Telnet connections to network devices. It provides a simple example of connecting to a network device, running commands, and saving the output. Additionally, you can automate the script to run at regular intervals.

## Features

- Connect to a network device using Telnet.
- Execute a series of commands on the device.
- Save the output to a text file.
- Log the date and time of task execution.
- Automate the script to run at 2-minute intervals.

## Prerequisites

- Python 3.x
- Telnetlib library (included with Python)
- apscheduler library

## Usage

1. Clone the repository to your local machine.

2. Install any required libraries using `pip`:

    ```bash
    pip install apscheduler
    ```

3. Modify the script to specify your Telnet connection details and the commands to be executed on the device.

4. Run the script:

    ```bash
    python APscheduler.py
    ```

    The script will run any scripts that you added to your APScheduler.py to be run in specific time mine is 2-min interval, and log the date and time of each time script run in `log-running-task.txt` for later reviewing.

5. used scheduling tool is [APScheduler](https://apscheduler.readthedocs.io/en/stable/) there is [cron](https://en.wikipedia.org/wiki/Cron) as well. 


## Acknowledgments

This script was developed as a basic example of automating network device tasks. You can extend it to meet your specific automation needs.

---

