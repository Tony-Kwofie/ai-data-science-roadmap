import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(
    r"C:\Users\HP\Desktop\PROJECTS\Vallberg Civitas Ltd - OHS Intelligence Platform\data\safety_incident_dataset.csv"
)

st.title("📊 Vallberg Civitas Ltd - OHS Intelligence Dashboard")

# --- FILTER SECTION ---
st.sidebar.header("🔍 Filter Incidents")
dept_filter = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
)
severity_filter = st.sidebar.multiselect(
    "Select Severity",
    options=df["Incident_Severity"].unique(),
    default=df["Incident_Severity"].unique(),
)

df_filtered = df[
    (df["Department"].isin(dept_filter))
    & (df["Incident_Severity"].isin(severity_filter))
]

# Show filtered data
st.dataframe(df_filtered)

# --- KPIs ---
st.subheader("📈 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Incidents", len(df_filtered))
col2.metric(
    "High Severity", df_filtered[df_filtered["Incident_Severity"] == "High"].shape[0]
)
col3.metric("Avg. Days Lost", round(df_filtered["Days_Lost"].mean(), 1))

# --- Incidents by Department ---
st.subheader("📌 Incidents by Department")
inc_by_dept = df_filtered["Department"].value_counts().reset_index()
inc_by_dept.columns = ["Department", "Incident Count"]

fig_dept = px.bar(
    inc_by_dept,
    x="Department",
    y="Incident Count",
    color="Incident Count",
    color_continuous_scale="Reds",
    title="Incident Frequency per Department",
)
st.plotly_chart(fig_dept, use_container_width=True)

# --- Severity Distribution ---
st.subheader("🎯 Incident Severity Distribution")
severity_counts = df_filtered["Incident_Severity"].value_counts().reset_index()
severity_counts.columns = ["Severity", "Count"]

fig_sev = px.pie(
    severity_counts, names="Severity", values="Count", title="Severity Breakdown"
)
st.plotly_chart(fig_sev, use_container_width=True)

# --- Root Cause Distribution ---
st.subheader("🧠 Root Cause Distribution")
root_cause = df_filtered["Root_Cause"].value_counts().reset_index()
root_cause.columns = ["Root Cause", "Count"]

fig_root = px.bar(
    root_cause,
    x="Root Cause",
    y="Count",
    title="Root Cause of Incidents",
    color="Count",
    color_continuous_scale="Blues",
)
st.plotly_chart(fig_root, use_container_width=True)

# --- Download Button ---
st.download_button(
    "📥 Download Filtered Data",
    df_filtered.to_csv(index=False),
    file_name="filtered_incidents.csv",
)
