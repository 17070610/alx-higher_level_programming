#!/bin/bash
# Takes in a URL, sends a request to it and displays
# the size of the bodyof the response
curl -s "$1" -o /dev/null -w '%{size_download}\n'
