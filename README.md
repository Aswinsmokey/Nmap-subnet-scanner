# Nmap Subnet Scanner

A script to automate Nmap scans across multiple subnets and save results in organized directories.

## Usage

1. Clone the repository.
2. pip install -r requirements.txt
3. Prepare a text file (`subnets.txt`) with subnets to scan.
4. Run the script with the following command:


python nmap-subnet-scanner.py -c "<nmap_command>" -o "<output_prefix>" -i "<subnets_file>" -s "<subnet_mask>"
