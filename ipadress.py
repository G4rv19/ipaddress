import re

ip_address = input("IPv4 address: ")

if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
    valid = True
    for i in ip_address.split('.'):
        if not (0 <= int(i) <= 255):
            valid = False
            break
    if valid:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")
else:
    print("Invalid format")
