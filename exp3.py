# Privacy Score Calculator

print("=================================")
print("     PRIVACY SCORE CALCULATOR")
print("=================================\n")

questions = [
    "Do you use a strong password?",
    "Do you use Two-Factor Authentication (2FA)?",
    "Do you regularly update your software?",
    "Do you use antivirus software?",
    "Do you use a VPN on public Wi-Fi?",
    "Is your social media profile private?",
    "Do you avoid clicking suspicious links?",
    "Do you review app permissions regularly?",
    "Do you use different passwords for different accounts?",
    "Do you avoid sharing personal information online?"
]

score = 0

for question in questions:
    answer = input(question + " (yes/no): ").strip().lower()

    if answer == "yes":
        score += 10

print("\n=================================")
print("            RESULTS")
print("=================================")

print(f"Privacy Score: {score}/100")

if score < 40:
    level = "Poor Privacy"
elif score < 60:
    level = "Average Privacy"
elif score < 80:
    level = "Good Privacy"
else:
    level = "Excellent Privacy"

print("Privacy Level:", level)

print("\nRecommendations:")

if score < 40:
    print("- Improve your online privacy practices.")
    print("- Use strong passwords and enable 2FA.")
elif score < 60:
    print("- Review privacy settings regularly.")
    print("- Consider using a VPN on public Wi-Fi.")
elif score < 80:
    print("- Good privacy protection.")
    print("- Continue following safe online habits.")
else:
    print("- Excellent privacy practices!")
    print("- Keep maintaining your security awareness.")

print("\nThank you for using Privacy Score Calculator!")