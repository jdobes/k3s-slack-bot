import os
import sys
import json

VERSION = "0.3.1"

CONFIG_FILE = "/etc/k3s_slack.json"
try:
    with open(CONFIG_FILE, "r") as fp:
        CFG_FILE = json.load(fp)
except FileNotFoundError:
    CFG_FILE = {}

SERVICE_MODE = "-s" in sys.argv

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
if not SLACK_BOT_TOKEN:
    SLACK_BOT_TOKEN = CFG_FILE.get("SLACK_BOT_TOKEN", "")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", "")
if not SLACK_APP_TOKEN:
    SLACK_APP_TOKEN = CFG_FILE.get("SLACK_APP_TOKEN", "")

BOT_GH_REPO_NAME = "k3s-slack-bot"
BOT_GH_REPO = f"https://github.com/jdobes/{BOT_GH_REPO_NAME}.git"
BOT_VERSION_CHECK_FILE = "k3s_slack/config.py"
BOT_INSTALLER_FILE = "install.sh"

K3S_INSTALLER_URL = "https://get.k3s.io"

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
GITHUB_UPDATES_CHANNEL_ID = "C02D25AJKPT"
