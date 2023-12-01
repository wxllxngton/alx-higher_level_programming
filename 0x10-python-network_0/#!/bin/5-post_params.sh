#!/bin/bash
# Script to post data (url-encoded) to a server

# Set the variables
email="test@gmail.com"
subject="I%20will%20always%20be%20here%20for%20PLD"

# Send POST request using curl
curl -s -d "email=$email&subject=$subject" -X POST "$1"
