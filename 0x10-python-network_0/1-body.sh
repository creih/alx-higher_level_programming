#!/bin/bash
# this one displays body of get
curl -s -o /dev/null -w "%{http_code}\n%{body}" "$1" | awk 'NR==1{if($1==200)print $2;else print "Error: Unexpected status code "$1}'
