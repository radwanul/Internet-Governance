
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV File
df = pd.read_csv("Digital_Divide_Survey_Dataset_30.csv")

# -------------------------
# Figure 1: Internet Access
# -------------------------
plt.figure(num="Figure 1: Internet Access Distribution", figsize=(6,6))
df["Internet_Access"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Figure 1: Internet Access Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()


# -------------------------
# Figure 2: Device Ownership
# -------------------------
plt.figure(num="Figure 2: Device Ownership", figsize=(7,5))
df["Device"].value_counts().plot(kind="bar")
plt.title("Figure 2: Device Ownership")
plt.xlabel("Device")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# -------------------------
# Figure 3: Urban vs Rural
# -------------------------
plt.figure(num="Figure 3: Urban vs Rural Respondents", figsize=(7,5))
df["Area"].value_counts().plot(kind="bar")
plt.title("Figure 3: Urban vs Rural Respondents")
plt.xlabel("Area")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# -------------------------
# Figure 4: Digital Skill
# -------------------------
plt.figure(num="Figure 4: Digital Skill Level", figsize=(8,5))
df["Digital_Skill"].value_counts().plot(kind="bar")
plt.title("Figure 4: Digital Skill Level")
plt.xlabel("Skill Level")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()