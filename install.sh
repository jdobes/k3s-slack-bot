#!/usr/bin/env bash

SOURCE_GIT="https://github.com/jdobes/k3s-slack-bot.git"
PYTHON_LIB_DIR="/usr/local/lib/python3.9/site-packages"
PYTHON_PACKAGE_NAME="k3s_slack"

install_deps () {
    dnf -y --best install python39 python39-pip git
    pip3 install -U slack_bolt requests
}

install_app () {
    rm -rf "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME"
    mkdir "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME"
    (
        if [ ! -d /tmp/k3s-slack-bot ]; then
            cd /tmp
            git clone "$SOURCE_GIT"
            cd k3s-slack-bot
        else
            cd /tmp/k3s-slack-bot
            git pull --rebase=false
        fi
        cp $PYTHON_PACKAGE_NAME/*.py "$PYTHON_LIB_DIR/$PYTHON_PACKAGE_NAME/"
        cp -f k3s-slack-bot.service /etc/systemd/system/k3s-slack-bot.service
    )
}

install_config () {
    config_file="/etc/k3s_slack.json"
    if [ ! -f $config_file ]; then
        cat <<EOF > $config_file
{
    "SLACK_BOT_TOKEN": "$SLACK_BOT_TOKEN",
    "SLACK_APP_TOKEN": "$SLACK_APP_TOKEN"
}
EOF
    fi
}

service_up () {
    systemctl enable k3s-slack-bot.service
    systemctl restart k3s-slack-bot.service
}

install_k3s () {
    curl -sfL https://get.k3s.io | sh -
}

install_deps
install_app
install_config
service_up

install_k3s
