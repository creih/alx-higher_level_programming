#!/bin/bash
# task 101 codesv for specified reqs
curl -sX POST -H "Content-Type: application/json" -d "@$2" $1 | grep -q "Valid JSON" && echo "Valid JSON" || echo "Not a valid JSON"
