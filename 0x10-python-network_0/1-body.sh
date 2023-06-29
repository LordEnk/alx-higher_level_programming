#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
#but only for responses with 200 status code

response=$(curl -sSL -w "$URL") #sent a Get request and store the response in a variable

statuscode=$(echo "$response" | head -n 1) #get the status code and body from the response
body=$(echo "$response" | tail -n =2)

if ["$statuscode" == "200" ]; then #display the body if the status code is 200
	echo "$body"
else
	echo "$statuscode"
fi
