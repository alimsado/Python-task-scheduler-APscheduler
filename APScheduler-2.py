from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime

def run_script_1():
    task_name = "Script 1"
    log_task_execution(task_name)
    exec(open("lab-1.py").read())

def run_script_2():
    task_name = "Script 2"
    log_task_execution(task_name)
    exec(open("lab-3.py").read())

def log_task_execution(task_name):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('log-running-task.txt', 'a') as log_file:
        log_file.write(f"{current_time} - {task_name} task executed.\n")

if __name__ == "__main__":
    # Create a scheduler
    scheduler = BackgroundScheduler()

    # Define triggers for each script
    trigger_1 = IntervalTrigger(minutes=1)  # First script runs every 1 minute
    trigger_2 = IntervalTrigger(minutes=2)  # Second script runs every 2 minutes

    # Add jobs to the scheduler
    scheduler.add_job(run_script_1, trigger=trigger_1)
    scheduler.add_job(run_script_2, trigger=trigger_2)

    # Start the scheduler
    scheduler.start()

    try:
        # Keep the script running
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler gracefully when you terminate the script
        scheduler.shutdown()
