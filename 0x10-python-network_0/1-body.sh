#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -I -s $1 | grep 200 | cut -d ' ' -f 2)" = "200" ]; then curl -X GET -s $1; fi
