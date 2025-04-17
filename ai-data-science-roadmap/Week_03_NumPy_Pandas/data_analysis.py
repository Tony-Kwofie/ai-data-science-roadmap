import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Desktop\tony python\data set\titanic.csv")

print(df.describe())

print(df["Survived"].value_counts())

print(df["Age"].mean())

print(df["Fare"].max())

print(df[(df["Sex"] == "female") & (df["Survived"] == 1)])

print(df["Pclass"].value_counts())

print(df.groupby("Sex")["Survived"].mean())

import matplotlib.pyplot as plt

df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived (1 = Yes, 0 = No)")
plt.ylabel("Number of Passengers")
plt.show()
