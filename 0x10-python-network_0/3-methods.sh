#!/bin/bash
# task to display http methods
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
