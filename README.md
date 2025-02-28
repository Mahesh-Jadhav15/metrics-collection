# System Metrics Collector

This project consists of three components:
1. **Python Script**: `collect_metrics.py` for reading and analyzing system metrics.
2. **Ansible Playbook**: `deploy_metrics_collector.yml` for automating the deployment of the metrics collector.
3. **Bash Script**: `collect_metrics.sh` for collecting CPU and memory usage statistics.

## Prerequisites

1. A remote VM with Ubuntu as the operating system.
2. Ansible installed for automating the deployment.
3. Python 3.x and the following Python libraries:
   - `paramiko`
   - `pandas`

## Setup Instructions

### Step 1: Set Up the Metrics Collector

1. **Deploying using Ansible**:
   - Ensure your Ansible is configured to access the remote VM.
   - Run the following command to copy and deploy the necessary scripts:
     ```bash
     ansible-playbook deploy_metrics_collector.yml
     ```

2. **Configure Log File**:
   - The playbook will ensure that the log file `/var/log/system_metrics.log` exists.

3. **Schedule Metrics Collection**:
   - The bash script `collect_metrics.sh` will be scheduled to run every minute using cron.

### Step 2: Python Analysis Script

<!-- Install the required Python libraries: -->
pip install paramiko pandas

1. **Run the Python Script**:
   - Replace the SSH connection details (`hostname`, `username`, `password`) in `collect_metrics.py` with the appropriate values.
   - Run the script to analyze the metrics collected by the bash script:
     ```bash
     python3 collect_metrics.py
     ```

2. **Metrics Analysis**:
   - The script will output:
     - The time of maximum CPU usage.
     - The time of maximum memory usage.
     - Daily average and median of CPU and memory usage.

## Customization

1. **Modify Log File Path**:
   - Change the log file path in both the bash and Python scripts if necessary.
   
2. **Adjust Cron Schedule**:
   - If you need a different schedule for metric collection, adjust the cron configuration in the Ansible playbook.

## Notes

- The Python script assumes the data in the log file is comma-separated with columns: `Timestamp`, `CPU Usage (%)`, and `Memory Usage (%)`.
- Ensuring the log file format is maintained by the bash script.
