import time
import numpy as np

from src.ingestion.tle_fetcher import fetch_tle
from src.ingestion.tle_reader import read_tle
from src.orbit.propagator import propagate
from src.avoidance.maneuver_planner import maneuver

from src.debris.fake_debris import get_debris_position
from src.collision.distance import distance_km
from src.collision.risk import collision_risk

TLE_PATH = "data/tle_live/active.tle"

# 🔹 TLE sirf ek baar fetch karo (safe for Celestrak)
fetch_tle(TLE_PATH)

while True:
    print("\n--- SYSTEM CYCLE START ---")

    # 1️⃣ Read ISS TLE
    name, tle1, tle2 = read_tle(TLE_PATH, satellite_name="ISS")

    # 2️⃣ Propagate ISS orbit
    position = propagate(tle1, tle2)

    # 3️⃣ Fake debris position (testing)
    debris_pos = get_debris_position(position)


    # 4️⃣ Distance calculation
    dist = distance_km(position, debris_pos)

    # 5️⃣ Risk + probability
    risk, probability = collision_risk(dist)

    # 6️⃣ Maneuver decision
    action = maneuver(probability)

    # 🔹 OUTPUT
    print(f"Satellite : {name}")
    print(f"Position  : {position}")
    print(f"DebrisPos : {debris_pos}")
    print(f"Distance  : {dist:.2f} km")
    print(f"Risk      : {risk}")
    print(f"Action    : {action}")

    print("--- SYSTEM CYCLE END ---")

    time.sleep(10)  # ⏱️ update every 10 seconds
