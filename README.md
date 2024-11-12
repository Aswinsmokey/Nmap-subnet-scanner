# Steps to Use the Script:
1. Download and Prepare the Script:
Make sure you have the script (nmap-subnet-scanner.py) ready on your system. You will also need Python installed (preferably Python 3.x).

2. Prepare Your Input File (subnets.txt):
Create a text file named subnets.txt that contains the list of subnets you want to scan. Each subnet should be listed on a new line, in CIDR notation (e.g., 10.60.10.0/24).

Example of subnets.txt:
192.168.1.0/24
192.168.2.0/24

3. Determine the Nmap Command:
The script allows you to run any Nmap command, such as -sV (service version scan), -p- (scan all ports), or any other custom Nmap command.
For example, to scan services (-sV), your Nmap command would look like nmap -sV.

5. Decide on the Subnet Mask:
You need to specify the subnet mask (e.g., /24, /27, etc.). The script will append this to each subnet in the file for scanning.

7. Run the Script:
Open a command prompt or terminal, and run the following command to start the script:

python nmap-subnet-scanner.py -c "nmap -sV" -o "service_scan" -i "subnets.txt" -s "/24"
Where:

-c "nmap -sV": Nmap command (in this example, service version scan).
-o "service_scan": Output file name prefix (e.g., 10.60.10.0_service_scan).
-i "subnets.txt": Path to the file containing your list of subnets.
-s "/24": Subnet mask (e.g., /24, /27).

# How the Script Works:
The script reads the subnets from subnets.txt and creates a folder for each subnet (based on the base address, not including the subnet mask).

It runs the specified Nmap command on each subnet and saves the output in the corresponding folder.
The output file will have a name like 10.60.10.0_service_scan depending on the provided -o prefix.

Example Output Structure:
For subnet 10.60.10.0/24, the script will create the folder Nmap_Scans/10.60.10.0 and save the scan results inside that folder. The file will be named like 10.60.10.0_service_scan.nmap, 10.60.10.0_service_scan.xml, and 10.60.10.0_service_scan.gnmap, depending on the output format.


