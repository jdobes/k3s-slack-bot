import os

VERSION = "0.0.1"
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", "")
INSTALLER_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/install.sh"
VERSION_CHECK_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/k3s_slack/config.py"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
