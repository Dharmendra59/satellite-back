def collision_risk(distance_km):
      if distance_km < 5:
        return "HIGH", 0.9
      elif distance_km < 20:
        return "MEDIUM", 0.6
      else:
        return "LOW", 0.1
