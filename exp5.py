daily_usage = float(input("Enter daily internet usage (GB): "))
days = int(input("Enter number of days: "))

total_usage = daily_usage * days

print("\nTotal Usage:", total_usage, "GB")

if total_usage < 50:
    print("Usage Level: Low")
elif total_usage < 200:
    print("Usage Level: Moderate")
else:
    print("Usage Level: High")