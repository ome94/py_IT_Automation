#!/bin/bash

# 
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"; free
echo

echo "JOBS"; jobs; echo
echo "Finishing at: $(date)"

#  We can also do these in a line 
# by adding a semi-colon
# at the end of each command

# echo "UPTIME"; uptime; echo
# echo "Starting at: $(date)"; echo
# echo "FREE"; free; echo
# echo "JOBS"; jobs; echo
# echo "Finishing at: $(date)"

