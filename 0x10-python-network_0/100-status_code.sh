#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response
url=$1
curl -so /dev/null --write-out "%{http_code}" "$1"
