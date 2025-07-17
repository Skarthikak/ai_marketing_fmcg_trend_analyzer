# scheduler.py
import schedule
import time
import subprocess

def run_analysis():
    print("Running trend analysis...")
    subprocess.run(["python", "main.py"])

# Run every hour
schedule.every(1).hour.do(run_analysis)

while True:
    schedule.run_pending()
    time.sleep(1)
