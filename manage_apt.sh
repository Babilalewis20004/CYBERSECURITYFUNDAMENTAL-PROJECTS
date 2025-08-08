#!/bin/bash

# First check if the script is run by the root user.
account=$(whoami)

if [ "$account" != "root" ]
then
    >&2 echo "This script must be run with superuser privileges."
    exit 1
fi

# If the user were root, execute the following code.
apt autoremove
apt update
apt full-upgrade -y

exit