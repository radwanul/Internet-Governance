import socket
import dns.resolver
import whois

domain = input("Enter domain name: ")

print("\nDNS INFORMATION")

# IP Address
try:
    ip = socket.gethostbyname(domain)
    print("IP Address:", ip)
except:
    print("IP Address not found")

# NS Record
try:
    print("\nName Servers:")
    for server in dns.resolver.resolve(domain, 'NS'):
        print(server.to_text())
except:
    print("NS Record not found")

# MX Record
try:
    print("\nMail Servers:")
    for mx in dns.resolver.resolve(domain, 'MX'):
        print(mx.to_text())
except:
    print("MX Record not found")

print("\nWHOIS INFORMATION")

try:
    info = whois.whois(domain)
    print("Registrar:", info.registrar)
    print("Creation Date:", info.creation_date)
    print("Expiration Date:", info.expiration_date)
except:
    print("WHOIS information unavailable")