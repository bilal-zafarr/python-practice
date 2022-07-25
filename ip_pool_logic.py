# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is: " + hostname)
# print("Your Computer IP Address is: " + IPAddr)

import ipaddress

ip_addr1 = ipaddress.ip_address(input("Enter IP address 1: "))

print(f"IP Address 1: {ip_addr1}")
print(type(ip_addr1))
print(dir(ip_addr1))