#!/bin/bash

# Get everything inside the folder
FILES=$(find *)

for file in $FILES
do
    
    # Change permissions using 644 which represents the permissions
    # mode for a file. 644 corresponds to -rw-r--r–.
    chmod 644 "$file"
done
