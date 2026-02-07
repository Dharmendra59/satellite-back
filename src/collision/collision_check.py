SAFE_DISTANCE = 5  # km

def collision_risk(dist):
    if dist < SAFE_DISTANCE:
        return "HIGH"
    return "LOW"
