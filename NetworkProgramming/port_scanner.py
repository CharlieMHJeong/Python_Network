#!/bin/python3
import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of args. ")
    print("Syntax: python3 scanner.py <ip>")


#Add a Banner
print("-" * 50)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)


try:
    for port in range(50,85): #(startingport, endingport)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result = s.connect_ex((target,port)) #returns an error indicator
        #print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExting Program!!")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to the server")
    sys.exit()
