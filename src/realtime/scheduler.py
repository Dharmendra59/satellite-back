import time
from src.ingestion.tle_fetcher import fetch_tle




def run_realtime():
while True:
fetch_tle()
print("TLE updated")
time.sleep(10)