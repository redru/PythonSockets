SET ACTION=%1

IF "%ACTION%"=="startup" (
    python bin/ftr-server.py
)

IF "%ACTION%"=="send" IF NOT [%2]==[] IF NOT [%3]==[] (
    python bin/ftr-cli.py %2 %3
)
