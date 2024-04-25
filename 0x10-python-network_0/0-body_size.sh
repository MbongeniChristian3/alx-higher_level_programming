#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get URL from command line argument
URL=$1

# Send request to URL using curl, discard headers, and get the size of the response body
SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Display the size of the response body in bytes
echo "Size of the response body: $SIZE bytes"

