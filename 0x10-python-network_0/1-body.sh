#!/bin/bash
# Script that takes in a URL, sends a GET request to it and displays the body of the response
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -L
