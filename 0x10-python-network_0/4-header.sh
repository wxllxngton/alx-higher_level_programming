#!/bin/bash
# Script sends GET request to URL, displays response body. Header X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$1"
