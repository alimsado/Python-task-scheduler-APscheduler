# Scheduler for Running Python Scripts

This repository contains two Python scripts that utilize the [APScheduler](https://apscheduler.readthedocs.io/en/stable/index.html) library to schedule and execute other Python scripts at specified intervals.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Scheduling a Single Script](#scheduling-a-single-script)
  - [Scheduling Multiple Scripts](#scheduling-multiple-scripts)
- [Customization](#customization)
- [Output and Logging](#output-and-logging)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x installed
- Required Python libraries (`apscheduler`, `datetime`)

To install the necessary libraries, you can use pip:

```bash
pip install apscheduler
```

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

## Usage

### Scheduling a Single Script

To schedule a single Python script to run at regular intervals, use `single_schedule.py`.

1. Edit `single_schedule.py` and replace `lab-1.py` with the filename of your script.

2. Run the script:

```bash
python single_schedule.py
```

This will schedule your script to run every 2 minutes. Adjust the interval as needed.

### Scheduling Multiple Scripts

To schedule multiple Python scripts to run at different intervals, use `multi_schedule.py`.

1. Edit `multi_schedule.py` and replace `lab-1.py` and `lab-3.py` with the filenames of your scripts. Adjust the intervals for each script.

2. Run the script:

```bash
python multi_schedule.py
```

This will schedule both scripts to run according to their specified intervals.

## Customization

- You can customize the script schedules by adjusting the interval triggers in the `multi_schedule.py` file.
- To add more scripts or modify the existing ones, edit the `run_script_1` and `run_script_2` functions in `multi_schedule.py`.

## Output and Logging

Both scripts provide logging functionality. They log the date and time of each script execution in a file named `log-running-task.txt`.

You can review the execution history by checking the `log-running-task.txt` file.

Outout of each scripts uploaded into `telnet_output.txt` file.

## Contributing

Contributions are welcome! If you'd like to enhance or fix issues in the scripts, please open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to replace `your-username/your-repo` with the actual GitHub repository URL where you intend to upload these scripts. This README will help users understand how to use and customize your scheduling scripts for running Python scripts at specific intervals.
