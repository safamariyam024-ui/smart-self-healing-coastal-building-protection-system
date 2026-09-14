def assess_risk(crack_percentage):
    """
    Prototype risk assessment based on detected crack area.
    
    NOTE:
    These thresholds are experimental prototype values,
    NOT certified structural engineering limits.
    """

    if crack_percentage < 0.5:
        risk = "LOW RISK"
        action = "SELF-HEALING SIMULATION"
        message = "Small crack detected. Suitable for prototype healing simulation."

    elif crack_percentage < 5.0:
        risk = "MEDIUM RISK"
        action = "INCREASE MONITORING + ENGINEER NOTIFICATION"
        message = "Moderate damage detected. Continue monitoring and notify an engineer."

    else:
        risk = "HIGH RISK"
        action = "STOP HEALING + ENGINEER ASSESSMENT"
        message = "High-risk damage detected. Autonomous healing is disabled."

    return {
        "risk": risk,
        "action": action,
        "message": message
    }


# Test the risk assessment
if __name__ == "__main__":

    test_values = [0.11, 1.46, 8.64]

    for crack_percentage in test_values:

        result = assess_risk(crack_percentage)

        print("\n--------------------------------")
        print(f"Crack Area : {crack_percentage}%")
        print(f"Risk Level : {result['risk']}")
        print(f"Action     : {result['action']}")
        print(f"Message    : {result['message']}")