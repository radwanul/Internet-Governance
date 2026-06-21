import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("exp7_internet_speed_dataset_240.csv")

# Basic Statistics
avg_speed = df["Speed_Mbps"].mean()
max_speed = df["Speed_Mbps"].max()
min_speed = df["Speed_Mbps"].min()

print("\n===== INTERNET SPEED REPORT =====")
print(f"Average Speed: {avg_speed:.2f} Mbps")
print(f"Maximum Speed: {max_speed:.2f} Mbps")
print(f"Minimum Speed: {min_speed:.2f} Mbps")

# Speed Classification
if avg_speed < 10:
    status = "Slow"
elif avg_speed < 50:
    status = "Moderate"
else:
    status = "Fast"

print(f"Status: {status}")

# Recommendation
if avg_speed < 10:
    print("Recommendation: Suitable for browsing and email only.")
elif avg_speed < 50:
    print("Recommendation: Suitable for HD streaming and online meetings.")
else:
    print("Recommendation: Suitable for gaming, 4K streaming, and large downloads.")

# Convert Timestamp to DateTime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Plot Graph
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["Speed_Mbps"], marker='o', markersize=3)

plt.title("Internet Speed Monitoring System")
plt.xlabel("Time")
plt.ylabel("Speed (Mbps)")
plt.grid(True)

plt.tight_layout()
plt.show()