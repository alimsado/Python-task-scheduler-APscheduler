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

## Usage

1. Clone the repository to your local machine.

2. Install any required libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Modify the script to specify your Telnet connection details and the commands to be executed on the device.

4. Run the script:

    ```bash
    python telnet_script.py
    ```

    The script will execute your specified commands, save the output to `telnet_output.txt`, and log the date and time of execution in `log-running-task.txt`.

5. If you want to automate the script to run at 2-minute intervals, consider using a scheduling tool like [APScheduler](https://apscheduler.readthedocs.io/en/stable/) or [cron](https://en.wikipedia.org/wiki/Cron). 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This script was developed as a basic example of automating network device tasks. You can extend it to meet your specific automation needs.

---

In the "Usage" section, I've added a note about automating the script using scheduling tools. You can also provide more specific instructions on setting up the automation if needed.
