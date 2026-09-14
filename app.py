import streamlit as st
import os

from cv_detection import detect_crack
from risk_assessment import assess_risk
from decision_engine import make_decision
from sensor_simulation import get_sensor_data


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Self-Healing Smart Coastal Protection",
    page_icon="🌊",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🌊 SELF-HEALING SMART COASTAL PROTECTION SYSTEM")

st.markdown(
    "### AI-Assisted Structural Monitoring, Risk Assessment & Safety Decision Platform"
)

st.divider()


# ============================================================
# SIDEBAR - SCENARIO SELECTION
# ============================================================

st.sidebar.title("🔍 SCENARIO CONTROL")

scenario = st.sidebar.radio(
    "Select structural condition:",
    [
        "Small Crack",
        "Medium Crack",
        "Large Crack"
    ]
)

image_files = {
     "Small Crack": "small_crack.jpg.jpeg",
     "Medium Crack": "medium_crack.jpg.jpeg",
     "Large Crack": "large_crack.jpg.jpeg"
}

image_path = image_files[scenario]


# ============================================================
# COMPUTER VISION
# ============================================================

if not os.path.exists(image_path):

    st.error(
        f"Image not found: {image_path}"
    )

    st.stop()


result = detect_crack(image_path)

crack_percentage = result["crack_percentage"]

risk_result = assess_risk(
    crack_percentage
)

decision_result = make_decision(
    risk_result["risk"]
)


# ============================================================
# SENSOR DATA
# ============================================================

sensor_data = get_sensor_data(
    risk_result["risk"]
)


# ============================================================
# TOP STATUS
# ============================================================

st.subheader("📊 LIVE STRUCTURAL STATUS")

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Scenario",
        scenario
    )


with c2:

    st.metric(
        "Crack Area",
        f"{crack_percentage:.2f}%"
    )


with c3:

    st.metric(
        "Detected Regions",
        result["crack_count"]
    )


with c4:

    if risk_result["risk"] == "LOW RISK":

        st.success("🟢 LOW RISK")

    elif risk_result["risk"] == "MEDIUM RISK":

        st.warning("🟡 MEDIUM RISK")

    else:

        st.error("🔴 HIGH RISK")


st.divider()


# ============================================================
# 1. DAMAGE DETECTION
# ============================================================

st.header("🔎 1. COMPUTER VISION DAMAGE DETECTION")

left, right = st.columns(2)


with left:

    st.subheader("Original Structure")

    st.image(
        image_path,
        width="stretch"
    )


with right:

    st.subheader("Detected Damage")

    if os.path.exists(result["output_path"]):

        st.image(
            result["output_path"],
            width="stretch"
        )


d1, d2 = st.columns(2)


with d1:

    st.metric(
        "Detected Regions",
        result["crack_count"]
    )


with d2:

    st.metric(
        "Approximate Crack Area",
        f"{crack_percentage:.2f}%"
    )


st.divider()


# ============================================================
# 2. SENSOR MONITORING
# ============================================================

st.header("🌊 2. STRUCTURAL & ENVIRONMENTAL MONITORING")

st.caption(
    "Sensor values shown here represent simulated monitoring inputs "
    "for the software demonstration."
)


s1, s2, s3 = st.columns(3)


with s1:

    st.metric(
        "🌊 Water Level",
        f"{sensor_data['Water Level']} m"
    )

    st.metric(
        "📏 Strain",
        f"{sensor_data['Strain']} %"
    )


with s2:

    st.metric(
        "📳 Vibration",
        f"{sensor_data['Vibration']} g"
    )

    st.metric(
        "🌡️ Temperature",
        f"{sensor_data['Temperature']} °C"
    )


with s3:

    st.metric(
        "💧 Humidity",
        f"{sensor_data['Humidity']} %"
    )

    st.metric(
        "⚙️ Corrosion Index",
        f"{sensor_data['Corrosion']} %"
    )


st.divider()


# ============================================================
# 3. RISK ANALYSIS
# ============================================================
# ============================================================
# SENSOR TREND MONITORING
# ============================================================

st.subheader("📈 SENSOR TREND MONITORING")

st.caption(
    "Trend values are simulated monitoring data for demonstration."
)

# Generate simulated historical values around the current readings

import pandas as pd
import random

trend_data = []

for i in range(10):

    trend_data.append({
        "Monitoring Point": i + 1,
        "Water Level": round(
            sensor_data["Water Level"] + random.uniform(-0.3, 0.3), 2
        ),
        "Strain": round(
            sensor_data["Strain"] + random.uniform(-0.05, 0.05), 2
        ),
        "Vibration": round(
            sensor_data["Vibration"] + random.uniform(-0.1, 0.1), 2
        )
    })

trend_df = pd.DataFrame(trend_data)

st.line_chart(
    trend_df.set_index("Monitoring Point"),
    width="stretch"
)
st.header("🧠 3. AI-ASSISTED RISK ASSESSMENT")


r1, r2 = st.columns(2)


with r1:

    st.subheader("Structural Risk")

    if risk_result["risk"] == "LOW RISK":

        st.success("🟢 LOW RISK")

    elif risk_result["risk"] == "MEDIUM RISK":

        st.warning("🟡 MEDIUM RISK")

    else:

        st.error("🔴 HIGH RISK")


with r2:

    st.subheader("Recommended Action")

    st.write(
        f"**{risk_result['action']}**"
    )


st.info(
    risk_result["message"]
)


st.divider()


# ============================================================
# 4. SAFETY DECISION ENGINE
# ============================================================

st.header("🛡️ 4. SAFETY DECISION ENGINE")


e1, e2, e3 = st.columns(3)


with e1:

    st.subheader("Decision")

    st.write(
        f"**{decision_result['decision']}**"
    )


with e2:

    st.subheader("Self-Healing")

    if decision_result["healing"]:

        st.success("🟢 ENABLED")

    else:

        st.error("🔴 DISABLED")


with e3:

    st.subheader("Engineer Alert")

    if decision_result["engineer_alert"]:

        st.warning("⚠️ REQUIRED")

    else:

        st.success("🟢 NOT REQUIRED")


if decision_result["engineer_alert"]:

    st.warning(
        decision_result["message"]
    )

else:

    st.success(
        decision_result["message"]
    )


st.divider()


# ============================================================
# 5. SELF-HEALING SYSTEM
# ============================================================

if risk_result["risk"] == "LOW RISK":

    st.header("🧬 5. SELF-HEALING SYSTEM")

    st.write(
        "Small suitable damage detected. "
        "A microcapsule-based healing process can be initiated."
    )


    h1, h2 = st.columns(2)


    with h1:

        st.metric(
            "Detected Crack Area",
            f"{crack_percentage:.2f}%"
        )


    with h2:

        st.metric(
            "Healing Status",
            "READY"
        )


    if st.button(
        "▶ START SELF-HEALING",
        type="primary"
    ):

        progress = st.progress(0)

        status = st.empty()


        status.info(
            "🔎 Stage 1: Crack detected"
        )

        progress.progress(20)


        status.info(
            "🧬 Stage 2: Microcapsule activated"
        )

        progress.progress(40)


        status.info(
            "💧 Stage 3: Healing agent released"
        )

        progress.progress(60)


        status.info(
            "🧱 Stage 4: Crack sealing in progress"
        )

        progress.progress(80)


        status.info(
            "📷 Stage 5: Camera verification"
        )

        progress.progress(100)


        st.success(
            "✅ SELF-HEALING COMPLETED"
        )


        # ----------------------------------------------------
        # HEALING VERIFICATION
        # ----------------------------------------------------

        st.subheader(
            "📊 HEALING VERIFICATION"
        )


        v1, v2 = st.columns(2)


        with v1:

            st.metric(
                "Before Healing",
                f"{crack_percentage:.2f}%"
            )


        simulated_after = crack_percentage * 0.15


        with v2:

            st.metric(
                "After Healing",
                f"{simulated_after:.2f}%"
            )


        if simulated_after < crack_percentage:

            st.success(
                "✅ HEALING VERIFIED — "
                "Detected crack region has been reduced."
            )


        st.caption(
            "⚠️ The post-healing value is a simulated "
            "prototype result. It does not represent "
            "validated physical material performance."
        )


# ============================================================
# 6. MEDIUM RISK RESPONSE
# ============================================================

elif risk_result["risk"] == "MEDIUM RISK":

    st.header("⚠️ 5. ENHANCED MONITORING")

    st.warning(
        "Moderate damage detected. "
        "Autonomous healing is not initiated."
    )


    m1, m2 = st.columns(2)


    with m1:

        st.metric(
            "Monitoring Level",
            "INCREASED"
        )


    with m2:

        st.metric(
            "Engineer Notification",
            "REQUIRED"
        )


    st.info(
        "The system continues remote monitoring "
        "while requesting professional engineering review."
    )


# ============================================================
# 7. HIGH RISK RESPONSE
# ============================================================

else:

    st.header("🚨 5. CRITICAL SAFETY RESPONSE")

    st.error(
        "HIGH-RISK DAMAGE DETECTED"
    )


    h1, h2, h3 = st.columns(3)


    with h1:

        st.metric(
            "Autonomous Healing",
            "STOPPED"
        )


    with h2:

        st.metric(
            "Engineer Assessment",
            "REQUIRED"
        )


    with h3:

        st.metric(
            "Remote Monitoring",
            "ACTIVE"
        )


    st.warning(
        "Autonomous healing is disabled. "
        "Professional engineering assessment is required."
    )


st.divider()


# ============================================================
# SYSTEM WORKFLOW
# ============================================================

st.header("⚙️ INTELLIGENT SYSTEM WORKFLOW")

st.markdown(
    """
### MONITOR
📷 Camera + Sensors

↓

### DETECT
🔎 Computer Vision

↓

### ANALYZE
🧠 Risk Assessment

↓

### DECIDE
🛡️ Safety Decision Engine

↓

### ACTION

🟢 **LOW RISK → SELF-HEAL**

🟡 **MEDIUM RISK → MONITOR + ENGINEER ALERT**

🔴 **HIGH RISK → STOP HEALING + ENGINEER ASSESSMENT**

↓

### VERIFY
📷 Post-action monitoring

↓

### CONTINUE MONITORING
🌊 Continuous structural observation
"""
)


st.divider()


# ============================================================
# SYSTEM COMPONENT STATUS
# ============================================================

st.header("📡 SYSTEM COMPONENT STATUS")

p1, p2, p3, p4 = st.columns(4)


with p1:

    st.success("📷 CAMERA\n\nACTIVE")


with p2:

    st.success("🔎 COMPUTER VISION\n\nACTIVE")


with p3:

    st.success("🌊 SENSOR MONITORING\n\nACTIVE")


with p4:

    if risk_result["risk"] == "HIGH RISK":

        st.error("🛡️ SAFETY STATUS\n\nCRITICAL")

    elif risk_result["risk"] == "MEDIUM RISK":

        st.warning("🛡️ SAFETY STATUS\n\nWARNING")

    else:

        st.success("🛡️ SAFETY STATUS\n\nNORMAL")


st.divider()


# ============================================================
# TECHNICAL NOTE
# ============================================================

st.caption(
    "The displayed sensor values and post-healing values are "
    "software-generated demonstration data. Physical deployment "
    "requires validated structural datasets, material testing, "
    "engineering analysis and field validation."
)
