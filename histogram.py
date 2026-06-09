import pandas as pd
import matplotlib.pyplot as plt

# Sample age data
ages = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45,
        50, 55, 60, 65, 70, 75, 80]

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=5)

plt.title("Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()