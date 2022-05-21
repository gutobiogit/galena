#!/bin/bash

python3 -m http.server 5500 &
python3 src/api.py &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?

