#!/bin/bash
#sends a request as an argument, and displays only the status code of the response.
curl --silent -o /dev/null -w "%{http_code}" "$1"
