#!/bin/bash
# Sends a GET request to a given URL with a header variable sent to a specific id
curl -sH "X-School-User-Id: 98" "${1}"
