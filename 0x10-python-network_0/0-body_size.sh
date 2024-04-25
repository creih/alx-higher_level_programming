#!/bin/bash
# Script: to get size of curl response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
