#!/bin/python3

# MURPHY'S PORT SCANNER

# Inspiration and walkthrough courtesy of TCM Security: Practical Ethical Hacking <https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course>

import sys
import socket
from datetime import datetime

# Define target IP address to scan

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translates hostname to IPv4
else:
    print("Invalid number of arguments provided")
    print("Proper syntax: python3 murphy_port_scanner.py <ip>")

# Make a banner for the process...

print("#" * 50)
print("LET THE SCANNING BEGIN!")
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))

try:
    for port in range(20,200): # Only scanning ports 20-200 for the time being
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nABORT! Cancelling the scan.")
    sys.exit()
    
except socket.gaierror:
    print("Oops... hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Sorry, could not connect to server")
    sys.exit() 