import streamlit as st
import pandas as pd
import joblib
import random
from datetime import datetime

# Load model and encoders
model = joblib.load(
    r"C:\Users\HP\Desktop\PROJECTS\Vallberg Civitas Ltd - OHS Intelligence Platform\models\model.pkl"
)
label_encoders = joblib.load(
    r"C:\Users\HP\Desktop\PROJECTS\Vallberg Civitas Ltd - OHS Intelligence Platform\models\label_encoders.pkl"
)

st.set_page_config(page_title="OHS Risk Predictor", layout="centered")

st.title("🧠 Vallberg Civitas Ltd | OHS Risk Predictor")
st.markdown(
    "Use this tool to **predict the risk level** of an incident before it occurs."
)

# Tooltip hints
st.info(
    "💡 Tip: Use realistic data to get better predictions. Click 'Test Mode' for auto-filled inputs."
)

# Option to run test mode
if st.checkbox("🧪 Test Mode"):
    location = random.choice(["Site A", "Site B", "Site C"])
    department = random.choice(["Maintenance", "Logistics", "Construction"])
    injury_type = random.choice(["Cut", "Burn", "Fracture", "Bruise", "Other"])
    root_cause = random.choice(["Human Error", "Mechanical Fault", "Negligence"])
    corrective_action = random.choice(["Training", "Repair", "Policy Update"])
    days_lost = random.randint(0, 30)
else:
    location = st.selectbox("📍 Location", ["Site A", "Site B", "Site C"])
    department = st.selectbox(
        "🏗 Department", ["Maintenance", "Logistics", "Construction"]
    )
    injury_type = st.selectbox(
        "💥 Injury Type", ["Cut", "Burn", "Fracture", "Bruise", "Other"]
    )
    root_cause = st.text_input("📌 Root Cause", value="Human Error")
    corrective_action = st.text_input("✅ Corrective Action", value="Training")
    days_lost = st.number_input("🕒 Estimated Days Lost", min_value=0, step=1)

# Predict button
if st.button("🔍 Predict Risk"):
    input_dict = {
        "Location": [location],
        "Department": [department],
        "Injury_Type": [injury_type],
        "Root_Cause": [root_cause],
        "Corrective_Action": [corrective_action],
        "Days_Lost": [days_lost],
    }
    input_df = pd.DataFrame(input_dict)

    # Encode categorical columns safely
    for col in label_encoders:
        if col in input_df.columns:
            input_df[col] = label_encoders[col].transform(input_df[col])
        else:
            st.warning(f"⚠️ Column '{col}' not found in input data. Skipping encoding.")

    prediction = model.predict(input_df)[0]
    risk_map = {0: "Low", 1: "Medium", 2: "High"}
    risk_color = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}
    risk_text = risk_map[prediction]

    st.success(f"Predicted Risk Level: {risk_color[risk_text]} **{risk_text}**")

    # Log prediction
    log_entry = input_dict.copy()
    log_entry["Predicted_Risk"] = risk_text
    log_entry["Timestamp"] = datetime.now()
    log_df = pd.DataFrame(log_entry)

    log_file = "predictions_log.csv"
    log_df.to_csv(
        log_file, mode="a", header=not pd.io.common.file_exists(log_file), index=False
    )
    st.caption(f"📝 Logged prediction to `{log_file}`")
