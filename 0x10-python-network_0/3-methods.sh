#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
if [ -z "$1" ]; then
	exit 1
fi

url=$1
response=$(curl -sL -I -X OPTIONS "$url")
aheader=$(echo "$response" | grep -i "ALLOW:")
hmethods=$(echo "$aheader" | awk -F ": " '{print $2}')
echo "hmethods"
