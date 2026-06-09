import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("population.csv")

# Create Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Age_Group"], df["Population"])

plt.title("Population Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Population")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()