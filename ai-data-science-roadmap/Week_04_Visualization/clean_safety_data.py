import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\tony python\data set\Occupational health and safety.csv"
)

# print(df.describe())

# Find out which columns have missing data:
# print(df.isnull().sum())


# Handle Missing Data
df.fillna({"Employee Age": df["Employee Age"].median()}, inplace=True)


df.fillna({"Duration (Days)": df["Duration (Days)"].mean()}, inplace=True)


# Fill missing Date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Re-convert to proper date

df["Date"] = df["Date"].ffill()  # Forward-fill missing dates (optional)

# Fill missing Severity
df["Severity"] = df["Severity"].fillna("Unknown")

# Fill missing comments
df["Comments"] = df["Comments"].fillna("No comment provided")

df.to_csv(
    r"C:\Users\HP\Desktop\tony python\data set\cleaned_occupational_health_and_safety.csv",
    index=False,
)


import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Load your cleaned data
df = pd.read_csv("cleaned_occupational_health_and_safety.csv")

# --- 1. Most Common Injury Types ---
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x="Injury Type",
    order=df["Injury Type"].value_counts().index,
    palette="Set2",
)
plt.title("Most Common Injury Types")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 2. Incidents by Location ---
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df, x="Location", order=df["Location"].value_counts().index, palette="Set3"
)
plt.title("Incidents by Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 3. Severity Distribution ---
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Severity", palette="coolwarm")
plt.title("Severity of Reported Incidents")
plt.tight_layout()
plt.show()

# --- 4. Employee Age vs. Duration (Days) ---
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x="Employee Age", y="Duration (Days)", hue="Severity", palette="Dark2"
)
plt.title("Employee Age vs Duration of Incident Recovery")
plt.tight_layout()
plt.show()
