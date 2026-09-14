import random


def get_sensor_data(risk_level):

    if risk_level == "LOW RISK":

        return {
            "Water Level": round(random.uniform(1.0, 2.0), 2),
            "Strain": round(random.uniform(0.10, 0.30), 2),
            "Vibration": round(random.uniform(0.10, 0.40), 2),
            "Temperature": round(random.uniform(27, 31), 1),
            "Humidity": round(random.uniform(60, 75), 1),
            "Corrosion": round(random.uniform(5, 15), 1)
        }

    elif risk_level == "MEDIUM RISK":

        return {
            "Water Level": round(random.uniform(2.0, 3.5), 2),
            "Strain": round(random.uniform(0.30, 0.70), 2),
            "Vibration": round(random.uniform(0.40, 0.80), 2),
            "Temperature": round(random.uniform(30, 34), 1),
            "Humidity": round(random.uniform(75, 85), 1),
            "Corrosion": round(random.uniform(15, 35), 1)
        }

    else:

        return {
            "Water Level": round(random.uniform(3.5, 5.0), 2),
            "Strain": round(random.uniform(0.70, 1.20), 2),
            "Vibration": round(random.uniform(0.80, 1.50), 2),
            "Temperature": round(random.uniform(34, 38), 1),
            "Humidity": round(random.uniform(85, 95), 1),
            "Corrosion": round(random.uniform(35, 60), 1)
        }