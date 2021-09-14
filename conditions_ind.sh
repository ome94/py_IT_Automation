#!/bin/bash

if (grep "127.0.0.1" /etc/hosts > /dev/null); then
    echo "Thumbs Up !"
else
    echo "ERROR: can't access localhost"
fi