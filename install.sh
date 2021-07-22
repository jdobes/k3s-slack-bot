#!/usr/bin/env bash

SOURCE_GIT="https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master"
PYTHON_LIB_DIR="/usr/local/lib/python3.9/site-packages"
PYTHON_PACKAGE_NAME="k3s_slack"

install_deps () {
    dnf -y --best install python39 python39-pip
    pip3 install -U slack_bolt requests
}

install_app () {
    rm -rf "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME"
    mkdir "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME"
    for f in __init__.py app.py config.py handlers.py utils.py; do
        curl -o "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME/$f" "$SOURCE_GIT/$PYTHON_PACKAGE_NAME/$f"
    done
}

install_config () {
    cat <<EOF > /etc/k3s_slack.json
{
    "SLACK_BOT_TOKEN": "$SLACK_BOT_TOKEN",
    "SLACK_APP_TOKEN": "$SLACK_APP_TOKEN"
}
EOF
}

install_deps
install_app
install_config
