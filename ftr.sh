#!/bin/bash
# Python path
PYTHONPATH="${PYTHONPATH}:libs"
export PYTHONPATH

# Read action to execute
ACTION="$1"

# Data for sending file
FILE="$2"
TARGET="$3"

if [ "$ACTION" == "startup" ]
    then python3 bin/ftr-server.py
fi

if [ "$ACTION" == "send" ]
    then python3 bin/ftr-cli.py $2 $3
fi

if [ "$ACTION" == "conf" ]
    then python3 bin/ftr-conf.py
fi
