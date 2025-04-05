#!/bin/bash

APP_DIR="$HOME/.nexcrypt"
INSTALL_PATH="/usr/local/bin"

mkdir -p "$APP_DIR"
cp nexcrypt.py "$APP_DIR"

echo "#!/bin/bash
python3 \"$APP_DIR/nexcrypt.py\" \"\$@\"" > nexcrypt
chmod +x nexcrypt

sudo mv nexcrypt /usr/local/bin/

echo "Installed 'nexcrypt' command to /usr/local/bin"
