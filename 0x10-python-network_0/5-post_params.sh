#!/bin/bash
# Script that sets email and subject variables, then sends a POST request using curl to the specified URL
email="test@gmail.com"
subject="I%20will%20always%20be%20here%20for%20PLD"
curl -s -d "email=$email&subject=$subject" -X POST "$1"
