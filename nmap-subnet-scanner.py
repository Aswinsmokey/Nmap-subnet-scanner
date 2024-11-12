import os
import subprocess
import argparse
from tqdm import tqdm  # Import tqdm for the progress bar

# Argument parsing
parser = argparse.ArgumentParser(description="Run Nmap on multiple subnets with custom output.")
parser.add_argument("-c", "--command", required=True, help="Nmap command to run on each subnet.")
parser.add_argument("-o", "--output", required=True, help="Base name for the output files.")
parser.add_argument("-i", "--input", required=True, help="File path for the list of subnets.")
parser.add_argument("-s", "--subnet", required=True, help="Subnet mask (e.g., /24, /27, /30) for scanning.")
args = parser.parse_args()

# Check if all required arguments are provided
if not args.command or not args.output or not args.input or not args.subnet:
    print("\nError: Missing arguments. Please provide the Nmap command, output file name prefix, subnet file, and subnet mask.")
    print("Usage: python nmap-subnet-scanner.py -c '<nmap_command>' -o '<output_base_name>' -i '<subnet_file>' -s '<subnet_mask>'")
    print("Example: python nmap-subnet-scanner.py -c 'nmap -sV' -o service_scan -i subnets.txt -s /24")
    exit(1)

# Nmap command, output base name, input file for subnets, and subnet mask
nmap_command = args.command
output_base_name = args.output
subnet_file = args.input
subnet_mask = args.subnet

# Directory where results will be stored
output_directory = "Nmap_Scans"
os.makedirs(output_directory, exist_ok=True)  # Create main directory if it doesn't exist

# Read the subnets from the specified file
try:
    with open(subnet_file, "r") as file:
        subnets = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Error: The file '{subnet_file}' was not found.")
    exit(1)

# Create a progress bar for the subnets
for subnet in tqdm(subnets, desc="Scanning Subnets", unit="subnet"):
    # Remove subnet mask from the folder name (keep only the base address)
    subnet_base = subnet.split('/')[0]  # Get the base subnet address (e.g., 10.85.10.0)

    # Create folder based on the base subnet address (e.g., 10.85.10.0)
    subnet_folder = os.path.join(output_directory, subnet_base)

    # Create the folder if it doesn't already exist
    if not os.path.exists(subnet_folder):
        os.makedirs(subnet_folder)

    # Define the output file prefix with the custom name provided by -o
    output_file_prefix = os.path.join(subnet_folder, f"{subnet_base}_{output_base_name}")

    # Prepare the full command by adding the subnet, subnet mask, and output option
    command = f"{nmap_command} {subnet}{subnet_mask} -oA {output_file_prefix}"

    # Run the command
    print(f"\nRunning command: {command}")
    subprocess.run(command, shell=True)

    print(f"Scan complete for {subnet}. Results saved in {subnet_folder}")
