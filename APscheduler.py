from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime

def run_my_script():
    # Import and execute your script here
    exec(open("lab-1.py").read())

if __name__ == "__main__":
    # Create a scheduler
    scheduler = BackgroundScheduler()

    # Define the trigger to run every 2 minutes
    trigger = IntervalTrigger(minutes=2)

    # Add the job to the scheduler
    scheduler.add_job(run_my_script, trigger=trigger)

    # Start the scheduler
    scheduler.start()

    try:
        # Keep the script running
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler gracefully when you terminate the script
        scheduler.shutdown()
