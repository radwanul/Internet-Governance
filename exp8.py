import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("exp8_Digital_Divide_Survey_Dataset_30.csv")

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
# DASHBOARD VIEW
# =====================================

fig, axes = plt.subplots(3, 2, figsize=(12, 10))

# Figure 1: Internet Access Distribution
df["Internet_Access"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Internet Access")
axes[0, 0].set_ylabel("")

# Figure 2: Device Ownership
df["Device"].value_counts().plot(
    kind="bar",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Device Ownership")
axes[0, 1].set_xlabel("Device")
axes[0, 1].set_ylabel("Respondents")

# Figure 3: Urban vs Rural
df["Area"].value_counts().plot(
    kind="bar",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Area Distribution")
axes[1, 0].set_xlabel("Area")
axes[1, 0].set_ylabel("Respondents")

# Figure 4: Digital Skill
df["Digital_Skill"].value_counts().plot(
    kind="bar",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Digital Skill Levels")
axes[1, 1].set_xlabel("Skill Level")
axes[1, 1].set_ylabel("Respondents")

# Figure 5: Daily Internet Usage
df["Daily_Usage_Hours"].plot(
    kind="hist",
    bins=8,
    ax=axes[2, 0]
)
axes[2, 0].set_title("Daily Internet Usage")
axes[2, 0].set_xlabel("Hours per Day")
axes[2, 0].set_ylabel("Respondents")

# Figure 6: Usage vs Digital Skill
skill_usage = df.groupby("Digital_Skill")["Daily_Usage_Hours"].mean()

skill_usage.plot(
    kind="bar",
    ax=axes[2, 1]
)

axes[2, 1].set_title("Usage vs Digital Skill")
axes[2, 1].set_xlabel("Skill Level")
axes[2, 1].set_ylabel("Average Hours")


plt.suptitle(
    "Digital Divide Survey Dashboard",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()
plt.show()