import os
import sys
import json

VERSION = "0.1.0"

CONFIG_FILE = "/etc/k3s_slack.json"
try:
    with open(CONFIG_FILE, "r") as fp:
        CFG = json.load(fp)
except FileNotFoundError:
    CFG = {}

SERVICE_MODE = "-s" in sys.argv

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
if not SLACK_BOT_TOKEN:
    SLACK_BOT_TOKEN = CFG.get("SLACK_BOT_TOKEN", "")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", "")
if not SLACK_APP_TOKEN:
    SLACK_APP_TOKEN = CFG.get("SLACK_APP_TOKEN", "")

INSTALLER_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/install.sh"
VERSION_CHECK_URL = "https://raw.githubusercontent.com/jdobes/k3s-slack-bot/master/k3s_slack/config.py"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
