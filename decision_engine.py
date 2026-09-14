def make_decision(risk_level):
    """
    Safety decision engine.

    The decision is rule-based so that critical actions
    are transparent and predictable.
    """

    if risk_level == "LOW RISK":
        return {
            "decision": "SELF-HEAL",
            "healing": True,
            "engineer_alert": False,
            "message": "Small suitable damage detected. Starting self-healing simulation."
        }

    elif risk_level == "MEDIUM RISK":
        return {
            "decision": "MONITOR + ALERT",
            "healing": False,
            "engineer_alert": True,
            "message": "Moderate damage detected. Increase monitoring and notify engineer."
        }

    elif risk_level == "HIGH RISK":
        return {
            "decision": "STOP HEALING",
            "healing": False,
            "engineer_alert": True,
            "message": "High-risk damage detected. Autonomous healing disabled. Engineer assessment required."
        }

    else:
        return {
            "decision": "UNKNOWN",
            "healing": False,
            "engineer_alert": True,
            "message": "Unknown risk condition. Engineer review required."
        }


# Test the decision engine
if __name__ == "__main__":

    risk_levels = [
        "LOW RISK",
        "MEDIUM RISK",
        "HIGH RISK"
    ]

    for risk in risk_levels:

        result = make_decision(risk)

        print("\n--------------------------------")
        print(f"Risk Level       : {risk}")
        print(f"Decision         : {result['decision']}")
        print(f"Self-Healing     : {result['healing']}")
        print(f"Engineer Alert   : {result['engineer_alert']}")
        print(f"Message          : {result['message']}")