import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv(r"C:\Users\HP\Desktop\tony python\data set\titanic.csv")

# Gender Filter
gender = st.selectbox("Select Gender", options=["all", "male", "female"])

if gender != "all":
    df = df[df["Sex"] == gender]

st.title("🚢 Titanic Data Dashboard")

# Pie Chart - Survival
st.subheader("🎯 Survival Distribution")
survival_counts = df["Survived"].value_counts()
labels = ["Did Not Survive", "Survived"]
fig1, ax1 = plt.subplots()
ax1.pie(survival_counts, labels=labels, autopct="%1.1f%%", startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# Bar Chart - Age vs Gender & Survival
st.subheader("📊 Average Age by Gender and Survival")
grouped_data = df.groupby(["Survived", "Sex"])["Age"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(x="Sex", y="Age", hue="Survived", data=grouped_data, ax=ax2)
ax2.set_title("Average Age by Gender and Survival")
st.pyplot(fig2)
