import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# --- DATABASE SETUP ---
conn = sqlite3.connect("incident_reports.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS reports (
    Incident_ID TEXT,
    Date TEXT,
    Location TEXT,
    Department TEXT,
    Injury_Type TEXT,
    Root_Cause TEXT,
    Corrective_Action TEXT,
    Incident_Severity TEXT,
    Days_Lost INTEGER
)
"""
)
conn.commit()

# --- TABS ---
tab1, tab2 = st.tabs(["📝 Submit Report", "📋 View Reports"])

# --- TAB 1: SUBMIT REPORT ---
with tab1:
    st.header("📝 Submit New Incident Report")

    incident_id = st.text_input("Incident ID")
    date = st.date_input("Date", datetime.today())
    location = st.selectbox("Location", ["Site A", "Site B", "Site C"])
    department = st.selectbox(
        "Department", ["Maintenance", "Logistics", "Construction"]
    )
    injury_type = st.selectbox(
        "Injury Type", ["Cut", "Burn", "Fracture", "Bruise", "Other"]
    )
    root_cause = st.text_input("Root Cause")
    corrective_action = st.text_area("Corrective Action")
    severity = st.selectbox("Incident Severity", ["Low", "Medium", "High"])
    days_lost = st.number_input("Days Lost", min_value=0, step=1)

    if st.button("Submit Report"):
        cursor.execute(
            """
            INSERT INTO reports (Incident_ID, Date, Location, Department, Injury_Type, Root_Cause,
                                 Corrective_Action, Incident_Severity, Days_Lost)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                incident_id,
                date,
                location,
                department,
                injury_type,
                root_cause,
                corrective_action,
                severity,
                int(days_lost),
            ),
        )
        conn.commit()
        st.success("✅ Incident report submitted successfully!")

# --- TAB 2: VIEW REPORTS ---
with tab2:
    st.header("📋 Submitted Incident Reports")
    df = pd.read_sql_query("SELECT * FROM reports", conn)

    if df.empty:
        st.info("No incident reports found.")
    else:
        st.dataframe(df, use_container_width=True)

        with st.expander("📥 Download Reports"):
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download as CSV", csv, "incident_reports.csv", "text/csv"
            )
