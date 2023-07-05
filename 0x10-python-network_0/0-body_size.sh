#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the respose
curl -sI "url" | grep "Content-Length:" | c7t -d ' ' -f2
