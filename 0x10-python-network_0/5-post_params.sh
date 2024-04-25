#!/bin/bash
# task for displaying body of post request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
