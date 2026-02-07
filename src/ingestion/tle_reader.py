def read_tle(filepath, satellite_name=None):
      with open(filepath, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

      if lines[0].startswith("<"):
            raise ValueError("Invalid TLE: HTML detected")

    # If specific satellite requested
      if satellite_name:
        for i in range(0, len(lines) - 2, 3):
            if satellite_name.lower() in lines[i].lower():
                return lines[i], lines[i+1], lines[i+2]

        raise ValueError(f"Satellite '{satellite_name}' not found in TLE file")

    # Else return first satellite
      return lines[0], lines[1], lines[2]
