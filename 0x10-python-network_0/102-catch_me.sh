#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton server
curl -s -X GET "0.0.0.0:5000/catch_me" > response.txt
if grep -q "You got me!" response.txt; then
	printf "$reponse.txt"
fi
rm response.txt
