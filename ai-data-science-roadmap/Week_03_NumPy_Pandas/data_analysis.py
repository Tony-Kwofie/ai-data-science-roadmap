import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Desktop\tony python\data set\titanic.csv")


print(df.describe())

# How many survived
print(df["Survived"].value_counts())

# Average age
print(df["Age"].mean())

# Highest fare
print(df["Fare"].max())

# Women who survived
print(df[(df["Sex"] == "female") & (df["Survived"] == 1)])

# How many people were in each class?
print(df["Pclass"].value_counts())

# Compare survival rate of men vs women:
print(df.groupby("Sex")["Survived"].mean())

import matplotlib.pyplot as plt

df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived (1 = Yes, 0 = No)")
plt.ylabel("Number of Passengers")
plt.show()
