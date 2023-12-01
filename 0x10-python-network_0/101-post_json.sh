#!/bin/bash
# ends a JSON POST request, displays the body of the response.
curl --silent --header "Content-Type: application/json" --data-raw "$(cat "$2")" "$1"
