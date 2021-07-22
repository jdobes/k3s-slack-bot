# k3s-slack-bot
Slack bot monitoring and managing k3s and deployed services

## Install script

    curl https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/install.sh | SLACK_BOT_TOKEN=token SLACK_APP_TOKEN=token bash -

- Installs on top of clean RHEL 8, installs Python and dependencies
- Deploys and enables Slack bot as systemd service
