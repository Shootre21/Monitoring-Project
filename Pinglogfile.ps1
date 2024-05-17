# Define the IP addresses to ping
$ipAddresses = @{
    "Google" = "8.8.8.8"
    "ERP" = "10.11.1.31"
    "DC1" = "10.11.1.11"
    "VSIFILE" = "10.11.1.21"
    "DC2" = "10.11.1.12"
    "VSI-TSFS" = "10.11.1.25"
    "VSI-RDS1" = "10.11.1.26"
    "VSI-RDS2" = "10.11.1.27"
    "VSI-RDS3" = "10.11.1.28"
}

# Set the interval in seconds (60 minutes = 3600 seconds)
$interval = 3600

# Set the log file path
$logFile = "ping_log.txt"

# Function to ping an IP address and log the result
function PingAndLog($name, $ip, $count) {
    Write-Host "Test $count In Progress..."
    $result = Test-Connection -ComputerName $ip -Count 60 | Select-Object ResponseTime
    $result | ForEach-Object {
        $log = "{0}`t{1}`t{2} ms" -f (Get-Date), $name, $_.ResponseTime
        Add-Content -Path $logFile -Value $log
    }
    Write-Host "Test $count Completed Log file results sent"
}

# Loop to ping each IP address every 60 minutes
$count = 1
while ($true) {
    $ipAddresses.GetEnumerator() | ForEach-Object {
        PingAndLog $_.Key $_.Value $count
    }
    $count++
    Start-Sleep -Seconds $interval
}

# Prompt the user to press any key to continue
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
