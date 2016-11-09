#!/bin/sh
ACTION="$1"
if [ ACTION=="STARTUP" ]; then
python bin/server.py
fi
