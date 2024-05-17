This Python script continuously monitors the status of specified servers and firewalls by pinging their IP addresses. Here's a summary and the purpose of the code:

### Summary
1. **IP Address Mapping**:
   - The script defines two dictionaries: `firewalls` and `servers`, mapping IP addresses to their respective names.

2. **Ping Function**:
   - `ping_server(ip_address)`: This function pings the given IP address once and returns `True` if the ping is successful (i.e., the server/firewall is up), and `False` otherwise.

3. **Monitoring Loop**:
   - `print_results()`: This function continuously pings all the servers and firewalls, collecting their statuses.
   - The results are displayed in a formatted table using the `tabulate` library.
   - The status is color-coded: green (`OK`) if the server/firewall is reachable, and red (`DOWN`) if it is not.
   - The terminal screen is cleared before each update to provide a real-time monitoring effect.
   - The script waits for 3 seconds before repeating the checks.

### Purpose
The primary purpose of this script is to monitor the connectivity status of a list of servers and firewalls. By periodically pinging these devices and displaying their statuses, administrators can quickly see which devices are operational and which are not. This real-time monitoring helps in promptly identifying and addressing network issues.
