#!/bin/bash

# Log file to store system metrics
LOG_FILE="/var/log/system_metrics.log"

# Create the log file if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    echo "Timestamp,CPU Usage (%),Memory Usage (%)" >> "$LOG_FILE"
fi

# Get the current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Collect CPU usage (percentage of CPU used)
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

# Collect memory usage (percentage of memory used)
MEMORY_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100}')

# Append the data to the log file
echo "$TIMESTAMP,$CPU_USAGE,$MEMORY_USAGE" >> "$LOG_FILE"

# Print a success message (optional, for debugging)
echo "Metrics logged at $TIMESTAMP: CPU=$CPU_USAGE%, Memory=$MEMORY_USAGE%"