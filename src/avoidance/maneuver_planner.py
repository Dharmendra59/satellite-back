def maneuver(collision_probability):
        if collision_probability >= 0.9:
                return {
                  "risk_level": "HIGH",
                  "action": "AVOIDANCE",
                  "delta_v": 0.15,              # km/s
                  "altitude_change": 2.0,       # km
                  "direction": "UP",
                  "note": "Emergency maneuver executed"
                }

    # 🟡 MEDIUM RISK
        elif collision_probability >= 0.4:
                return {
                  "risk_level": "MEDIUM",
                  "action": "MONITOR",
                  "delta_v": 0.05,
                  "altitude_change": 0.5,
                  "direction": "SLIGHT_UP",
                  "note": "Minor correction applied"
                }

    # 🟢 LOW RISK
        else:
                return {
                  "risk_level": "LOW",
                  "action": "NONE",
                  "delta_v": 0.0,
                  "altitude_change": 0.0,
                  "direction": "STABLE",
                  "note": "No maneuver required"
                }
