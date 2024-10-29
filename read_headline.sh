#!/bin/bash

# Prompt the user to enter the day and month
read -p "Enter the day (DD) to read the headlines (e.g., 29): " day
read -p "Enter the month (MM) to read the headlines (e.g., 10): " month

# Get the current year
year=$(date +%Y)

# Construct the filename based on user input
filename="headlines_${year}-${month}-${day}.csv"

# Check if the file exists
if [ -f "$filename" ]; then
    # Read the file using less
    less "$filename"
else
    echo "File $filename not found."
fi
