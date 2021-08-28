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

BOT_GH_REPO = "jdobes/k3s-slack-bot"
INSTALLER_URL = f"https://raw.githubusercontent.com/{BOT_GH_REPO}/master/install.sh"
VERSION_CHECK_URL = f"https://raw.githubusercontent.com/{BOT_GH_REPO}/master/k3s_slack/config.py"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
GITHUB_UPDATES_CHANNEL_ID = "C02D25AJKPT"
