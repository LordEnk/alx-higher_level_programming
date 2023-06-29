#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

response=$(curl -sSL "URL") #send a GET request and store the response in a variable
size=$(echo -n "$response" | wc -c) #calculate the size of the response body
echo "$size" #display the size of the response body
