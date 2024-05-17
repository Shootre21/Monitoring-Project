import os
import time
import platform
import subprocess
from tabulate import tabulate

firewalls = {
    "xxxxxxxx: "Albany",
    "xxxxxxxx": "Cortland",
    "xxxxxxxx": "Gainsville",
    "xxxxxxxx": "Fresno",
    "xxxxxxxx": "Modesto",
    "xxxxxxxx": "Nacogdoches",
    "xxxxxxxx": "Riverside",
    "xxxxxxxx": "Salida",
    "xxxxxxxx": "Springdale",
    "xxxxxxxx": "Vislia",
}

servers = {
    "xxxxxxxx": "MITS",
    "xxxxxxxx": "Veeam",
    "xxxxxxxx": "DC1",
    "xxxxxxxx": "VSIFILE",
    "xxxxxxxx": "DC2",
    "xxxxxxxx": "VSI-TSFS",
    "xxxxxxxx": "VSI-RDS1",
    "xxxxxxxx": "VSI-RDS2",
    "xxxxxxxx": "VSI-RDS3",
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
