#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response

response=$(curl -sSL -w "$URL"); statuscode=$(echo "$response" | head -n 1); body=$(echo "$response" | tail -n =2); if ["$statuscode" == "200" ]; then echo "$body"; else echo "$statuscode";fi
