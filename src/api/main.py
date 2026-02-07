from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.ingestion.tle_reader import read_tle
from src.orbit.propagator import propagate
from src.avoidance.maneuver_planner import maneuver

TLE_PATH = "data/tle_live/active.tle"

app = FastAPI()

# 🔹 CORS (React ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ✅ ROOT ENDPOINT (ye missing tha)
@app.get("/")
def root():
    return {
        "status": "Space Debris AI Backend Running",
        "endpoints": ["/position"]
    }

# ✅ POSITION API (React yahin hit karega)
@app.get("/position")
def position():
    # ISS TLE read
    name, tle1, tle2 = read_tle(TLE_PATH, satellite_name="ISS")

    # Orbit propagation
    x, y, z = propagate(tle1, tle2)

    # Dummy risk (later AI/RL se aayega)
    probability = 0.8
    action = maneuver(probability)

    return {
        "satellite": name,
        "x": x,
        "y": y,
        "z": z,
        "maneuver": action
    }
