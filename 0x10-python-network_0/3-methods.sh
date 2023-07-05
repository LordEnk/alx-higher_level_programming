#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept

url=$1
hmethods=$(curl -sL -I -X OPTIONS "$1" | grep -i "ALLOW:" | awk -F ": " '{print $2}')
echo "$hmethods"

