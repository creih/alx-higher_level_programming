#!/bin/bash
# advanced task about displaying status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") echo "$status_code"
