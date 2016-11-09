#!/bin/sh
ACTION="$1"
if [ ACTION == "startup" ]
    then python bin/server.py
fi

if [ ACTION == "send" ]
    then python bin/client.py $2 $3
