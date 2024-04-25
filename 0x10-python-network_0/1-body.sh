#!/bin/bash
# this one displays body of get
[ $# -ne 1 ] && echo "Usage: $0 <URL>" && exit 1; curl -s -o response.txt -w "%{http_code}" "$1" > /dev/null; status_code=$(tail -n 1 response.txt); [ "$status_code" -eq 200 ] && curl -s "$1" || echo "Error: Status code $status_code"
