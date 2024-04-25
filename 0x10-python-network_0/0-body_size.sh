#!/usr/bin/env bash
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

temp_file=$(mktemp)
curl -s -o "$temp_file" -w "%{size_download}" "$url" > /dev/null

size=$(cat "$temp_file")

echo "Size of the response body: $size bytes"

rm "$temp_file"
