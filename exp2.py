# Website Cookie and Tracker Analyzer

url = input("Enter website URL: ")

print("\n=================================")
print(" WEBSITE COOKIE & TRACKER ANALYZER")
print("=================================")

if "https://" in url:
    print("Secure Connection (HTTPS): Yes")
else:
    print("Secure Connection (HTTPS): No")

print("\nPossible Trackers and Cookies:")

trackers = [
    "Session Cookies",
    "Analytics Cookies",
    "Advertising Cookies",
    "Social Media Trackers"
]

for tracker in trackers:
    print("-", tracker)

print("\nPrivacy Recommendation:")
print("- Review cookie settings before accepting.")
print("- Block unnecessary third-party cookies.")
print("- Use privacy-focused browser extensions.")