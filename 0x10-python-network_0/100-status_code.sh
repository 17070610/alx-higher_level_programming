#!/bin/bash
# Sends arequest to a give URL, and displays the status code of teh response
curl -s -o /dev/null -w "%{http_code}" "$1"
