import requests
import time

TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

def fetch_tle(save_path):
    headers = {
        "User-Agent": "Space-Debris-AI/1.0 (Educational Project)"
    }

    response = requests.get(TLE_URL, headers=headers, timeout=15)

    if response.status_code != 200:
        raise RuntimeError(f"TLE fetch failed: HTTP {response.status_code}")

    if response.text.startswith("<"):
        raise RuntimeError("Blocked by source (HTML received)")

    with open(save_path, "w") as f:
        f.write(response.text)

    print("TLE fetched successfully")

    # 🔒 RATE LIMIT (VERY IMPORTANT)
    time.sleep(5)  # safe delay
