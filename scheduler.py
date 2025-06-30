import schedule
import time
import os
from dotenv import load_dotenv
from task_bots.Qreserve import run_bot

# Load environment variables from .env
load_dotenv()

# Fetch scheduled time from .env
SCHEDULE_TIME = os.getenv("BOOKING_TIME", "08:00")

def schedule_jobs():
    print(f"[Scheduler] Scheduling bot run at {SCHEDULE_TIME} daily.")
    schedule.every().day.at(SCHEDULE_TIME).do(run_bot)

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[Scheduler] Scheduler stopped manually.")

if __name__ == "__main__":
    schedule_jobs()
