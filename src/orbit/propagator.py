from sgp4.api import Satrec, jday
from datetime import datetime

def propagate(tle1, tle2):
    sat = Satrec.twoline2rv(tle1, tle2)

    now = datetime.utcnow()

    jd, fr = jday(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    error, position, velocity = sat.sgp4(jd, fr)

    if error != 0:
        print(f"[WARNING] SGP4 error code: {error} (continuing)")

    return position  # (x, y, z) km
