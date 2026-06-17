import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Digital_Divide_Survey_Dataset_30.csv")

# =====================================
# SURVEY SUMMARY
# =====================================

print("=====================================")
print("   DIGITAL DIVIDE SURVEY DASHBOARD")
print("=====================================")

print("\nTotal Respondents:", len(df))

internet_rate = (df["Internet_Access"] == "Yes").mean() * 100

print(f"Internet Access Rate: {internet_rate:.2f}%")

print("\nArea Distribution:")
print(df["Area"].value_counts())

print("\nDevice Distribution:")
print(df["Device"].value_counts())

print("\nDigital Skill Levels:")
print(df["Digital_Skill"].value_counts())


# =====================================
# Figure 1: Internet Access Distribution
# =====================================

plt.figure(figsize=(6,6))
df["Internet_Access"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Figure 1: Internet Access Distribution")
plt.ylabel("")
plt.show()


# =====================================
# Figure 2: Device Ownership
# =====================================

plt.figure(figsize=(7,5))
df["Device"].value_counts().plot(kind="bar")
plt.title("Figure 2: Device Ownership")
plt.xlabel("Device")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.show()


# =====================================
# Figure 3: Urban vs Rural Respondents
# =====================================

plt.figure(figsize=(7,5))
df["Area"].value_counts().plot(kind="bar")
plt.title("Figure 3: Urban vs Rural Respondents")
plt.xlabel("Area")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.show()


# =====================================
# Figure 4: Digital Skill Level
# =====================================

plt.figure(figsize=(7,5))
df["Digital_Skill"].value_counts().plot(kind="bar")
plt.title("Figure 4: Digital Skill Level")
plt.xlabel("Skill Level")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.show()


# =====================================
# Figure 5: Daily Internet Usage
# =====================================

plt.figure(figsize=(7,5))
df["Daily_Usage_Hours"].plot(
    kind="hist",
    bins=8
)
plt.title("Figure 5: Daily Internet Usage")
plt.xlabel("Hours per Day")
plt.ylabel("Number of Respondents")
plt.show()