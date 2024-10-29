#!/bin/bash

# Prompt the user to enter the date
read -p "Enter the date (DD) to read the headlines (e.g., 29): " day

# Get the current month and year
month=$(date +%m)
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
