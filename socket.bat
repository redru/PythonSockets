SET ACTION=%1

IF "%ACTION%"=="startup" (
    python bin/server.py
)

IF "%ACTION%"=="send" IF NOT [%2]==[] IF NOT [%3]==[] (
    python bin/client.py %2 %3
)
