# Internet Speed Monitoring System

speed = float(input("Enter internet speed (Mbps): "))

print("\n========================")
print(" INTERNET SPEED REPORT")
print("========================")

print("Current Speed:", speed, "Mbps")

if speed < 10:
    status = "Slow"
elif speed < 50:
    status = "Moderate"
else:
    status = "Fast"

print("Speed Status:", status)

if speed < 10:
    print("Recommendation: Suitable for browsing and email only.")
elif speed < 50:
    print("Recommendation: Suitable for HD streaming and online meetings.")
else:
    print("Recommendation: Suitable for gaming, 4K streaming, and large downloads.")