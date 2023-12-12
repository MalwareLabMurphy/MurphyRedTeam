#!/bin/python3

# MURPHY'S SIMPLE FUZZER

# Inspiration and walkthrough courtesy of TCM Security: Practical Ethical Hacking <https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course>

import sys
import socket
from time import sleep

# Create buffer to test

buffer= "A" * 100

# Set variables for target

ip=input("What is the target IP address?")
port=input("What is the target port?")
command=input("What command will we fuzz?")

# Loop for testing buffer

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        
        payload= command + buffer

        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer=buffer + "A"*100
        
    except:
        print ("Fuzzing attempt crashed at %s bytes!" % str(len(buffer)))
        sys.exit()