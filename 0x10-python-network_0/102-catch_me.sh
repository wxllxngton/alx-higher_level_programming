#!/bin/bash

# Send a POST request to 0.0.0.0:5000/catch_me with the custom header "Origin: ALX"
curl -s -X PUT -H "Origin: ALX" -d "user_id=98" 0.0.0.0:5000/catch_me
