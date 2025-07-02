import time
import os
from dotenv import load_dotenv
from task_bots.Qreserve import run_bot
from datetime import datetime
import sys

TESTFLAG = False
# Load environment variables from .env
load_dotenv()

# Fetch scheduled time from .env
SCHEDULE_DATE = os.getenv("SCHEDULE_DATE")  # Format: YYYY-MM-DD
SCHEDULE_TIME = os.getenv("SCHEDULE_TIME")  # Format: HH:MM (24-hour)

def schedule_jobs():
    now = datetime.now()
    print(f"[Scheduler] Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    if sys.argv[1] == 'test':
        now = datetime.now()
        print(f"[Scheduler] Testing time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        run_bot(True)
        print("[Scheduler] Test finished. Exiting scheduler.")
        return
    else:
        if not SCHEDULE_DATE or not SCHEDULE_TIME:
            print("[Scheduler] ERROR: BOOKING_DATE or BOOKING_TIME not set in .env.")
            return
        
        try:
            scheduled_dt = datetime.strptime(f"{SCHEDULE_DATE} {SCHEDULE_TIME}", "%Y-%m-%d %H:%M")
            print(f"[Scheduler] Bot will run at: {scheduled_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError:
            print("[Scheduler] ERROR: Invalid date/time format. Use YYYY-MM-DD and HH:MM (24-hour).")
            return
        
        while True:
            now = datetime.now()
            try:
                if now >= scheduled_dt:
                    print(f"[Scheduler] Time reached: {now.strftime('%Y-%m-%d %H:%M:%S')}")
                    run_bot(False)
                    print("[Scheduler] Bot finished. Exiting scheduler.")
                    break
                time.sleep(5)  # Check every 60 seconds
            except KeyboardInterrupt:
                print("\n[Scheduler] Scheduler stopped manually.")

if __name__ == "__main__":
    schedule_jobs()
