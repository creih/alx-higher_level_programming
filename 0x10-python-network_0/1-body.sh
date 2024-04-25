#!/bin/bash
# this one displays body of get
curl -s "$1" | tail -n 1
