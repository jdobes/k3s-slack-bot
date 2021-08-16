import os

VERSION = "0.0.2"
CONFIG_FILE = "/etc/k3s_slack.json"
INSTALL_LOCATION = "/usr/local/lib/python3.9/site-packages/k3s_slack"
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", "")
INSTALLER_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/install.sh"
VERSION_CHECK_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/k3s_slack/config.py"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
