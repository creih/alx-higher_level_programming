#!/bin/bash
# advanced task about displaying status code
echo "$(status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1"))"
