# Project Title
IPGenerator_PortScanner

## Getting Started
This application is going to generate IPs from the given network and scan ports(ports.txt).

### System requirement
Please install python 3.7.4 and run it on Windows.

### Feature Requirement
1.	All IP addresses generated must fall within the subnet input by the end-user 
•	the end-user will be prompted to provide the subnet and subnet mask when the script first starts 
•	for example: subnet 192.168.x with subnet mask of 255.255.255.0 
2.	The script must skip every IP address that is evenly numbered (divisible by 2) 
•	for example: 192.168.0.12, 192.168.0.14, … , 192.168.0.252, 192.168.0.254 
3.	Reserves the top 10 IP addresses for printers and servers 
4.	scan all ports for each of the IP addresses in the subnet  
•	the ports are defined a file (ports.txt) that is imported when the script starts  
•	outputs the status of each port (open or closed) 
5.	the script must output the IP address and port status to: 
•	console 
•	log file (ip_port_log.txt)
•	Windows Event Viewer (IP Addresses Only)

### Running the tests
1.	Put all the files in the same directory
2.	Please prepare ports.txt file 
3.	Run “xyzit_port_scanner.py” 
4.	If Enter proper IP network address when it prompts:
Please enter a network address(IPAddress/sm):
5.	Please check console or ip_port_log.txt file for the result.

### Bug Fixes:

### Release Notes:
#1.0.0 - CJ 29.05.2020 First draft
