import paramiko
import pandas as pd
from io import StringIO

# SSH connection details
hostname = ""  # Replace with your remote VM's IP
username = "ubuntu"      
password = ""  # Replace with your remote VM's password
log_file = "/var/log/system_metrics.log"

# Connect to the remote VM using SSH
print("Connecting to the remote VM...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Read the log file
print(f"Reading log file from {log_file}...")
stdin, stdout, stderr = ssh.exec_command(f"cat {log_file}")
log_data = stdout.read().decode()

# Close the SSH connection
ssh.close()
print("SSH connection closed.")

# Load the log data into a Pandas DataFrame
print("Analyzing the data...")
df = pd.read_csv(StringIO(log_data), parse_dates=["Timestamp"])

# a. Max CPU usage and corresponding time
max_cpu = df.loc[df["CPU Usage (%)"].idxmax()]
print(f"\nMax CPU Usage: {max_cpu['CPU Usage (%)']}% at {max_cpu['Timestamp']}")

# b. Max Memory usage and corresponding time
max_memory = df.loc[df["Memory Usage (%)"].idxmax()]
print(f"Max Memory Usage: {max_memory['Memory Usage (%)']}% at {max_memory['Timestamp']}")

# c. Daily Average and Median CPU and Memory usage
df.set_index("Timestamp", inplace=True)
daily_avg = df.resample("D").mean()
daily_median = df.resample("D").median()

print("\nDaily Average CPU and Memory Usage:")
print(daily_avg)

print("\nDaily Median CPU and Memory Usage:")
print(daily_median)