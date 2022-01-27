#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    # $file is wrapped in ""
    # to ensure it works eve when filenames contain spaces
    #  thus requiring a "" when basename is called.
    echo mv "$file" "$name.html"
done;
