# Fake Link Warning Tool

url = input("Enter a URL: ").lower()

print("\n========================")
print(" FAKE LINK ANALYZER")
print("========================")

reasons = []

if "https://" not in url:
    reasons.append("URL does not use HTTPS.")

suspicious_words = ["login", "verify", "secure", "update", "free", "bank"]

for word in suspicious_words:
    if word in url:
        reasons.append(f"Contains suspicious keyword: {word}")

if reasons:
    print("Warning: This link may be suspicious!\n")
    
    for reason in reasons:
        print("-", reason)
else:
    print("This link appears safe.")