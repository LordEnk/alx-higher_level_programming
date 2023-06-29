#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and 
#displays the body of the response
response=$(curl -sSL -X DELETE "$url") #send the delete request and store result in a variable
echo "$response" #display the response
