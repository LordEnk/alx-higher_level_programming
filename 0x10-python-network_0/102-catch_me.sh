#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton server
curl -s -X GET 0.0.0.0:5000/catch_me >&1
