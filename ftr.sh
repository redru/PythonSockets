#!/bin/bash
# Read action to execute
ACTION="$1"

# Data for sending file
FILE="$2"
TARGET="$3"

# Data for configuration
USER="$2"

if [ "$ACTION" == "startup" ]
    then python bin/ftr-server.py
fi

if [ "$ACTION" == "send" ]
    then python bin/ftr-cli.py $2 $3
fi

if [ "$ACTION" == "conf" ]
    then python bin/conf.py
fi
