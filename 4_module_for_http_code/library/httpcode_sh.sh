#!/bin/bash
# WANT_JSON

address=$(cat $1 | grep -Po '(?<="address": ")(.*?)(?=")')

http_response=`curl -s -o /dev/null -w "%{http_code}" $address`

if [[ $http_response == "000" ]]; then
    failed="true"
    msg="Wrong address!"
elif [[ $http_response == "200" ]]; then
    msg="Success"
else
    msg="Got HTTP error responce"
fi

echo "{\"http_response\": \"$http_response\", \"failed\": \"$failed\", \"msg\": \"$msg\", \"changed\": \"true\"}"