#!/bin/bash

echo "Removing nexcrypt..."

# Remove binary
sudo rm -f /usr/local/bin/nexcrypt

# Remove nexcrypt storage
rm -rf "$HOME/.nexcrypt"

echo "nexcrypt has been removed from your system."
