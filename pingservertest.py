import os
import time
import platform
import subprocess
from tabulate import tabulate

firewalls = {
    "10.11.1.1": "Albany",
    "10.70.1.1": "Cortland",
    "10.50.1.1": "Gainsville",
    "10.2.1.1": "Fresno",
    "10.1.1.1": "Modesto",
    "10.35.1.1": "Nacogdoches",
    "10.5.1.1": "Riverside",
    "10.20.1.1": "Salida",
    "10.40.1.1": "Springdale",
    "10.12.1.1": "Vislia",
}

servers = {
    "10.11.1.32": "MITS",
    "10.11.1.13": "Veeam",
    "10.11.1.11": "DC1",
    "10.11.1.21": "VSIFILE",
    "10.11.1.12": "DC2",
    "10.11.1.25": "VSI-TSFS",
    "10.11.1.26": "VSI-RDS1",
    "10.11.1.27": "VSI-RDS2",
    "10.11.1.28": "VSI-RDS3",
}

def ping_server(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    return subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def print_results():
    while True:
        server_results = []
        firewall_results = []

        for ip, name in servers.items():
            status = "OK" if ping_server(ip) else "DOWN"
            color = '\033[92m' if status == "OK" else '\033[91m'
            status = f"{color}{status}\033[0m"
            server_results.append([name, status])

        for ip, name in firewalls.items():
            status = "OK" if ping_server(ip) else "DOWN"
            color = '\033[92m' if status == "OK" else '\033[91m'
            status = f"{color}{status}\033[0m"
            firewall_results.append([name, status])

        os.system('cls' if platform.system().lower() == 'windows' else 'clear')
        print(tabulate(server_results, headers=['Server', 'Status'], tablefmt='grid'))
        print("\nFirewalls:")
        print(tabulate(firewall_results, headers=['Firewall', 'Status'], tablefmt='grid'))
        time.sleep(3)

if __name__ == "__main__":
    print_results()