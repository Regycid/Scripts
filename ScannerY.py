#!/bin/python3

import sys
import socket
from datetime import datetime

#Target definition
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #IPV4 Translation
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 ScannerY.py <ip>")
	
#Banner
print("-" * 40)
print("Scanning target "+target)
print("@ "+str(datetime.now()))
print("-" * 40)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("port{} is open".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\nStopping")
	sys.exit()

except socket.gaierror:
	print("Hostname couldn't be resolved")
	sys.exit()
	 
except socket.error:
	print("Couldn't connect to server")
	sys.exit()
	