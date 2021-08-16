import os

import requests

from k3s_slack.config import VERSION, VERSION_CHECK_URL, INSTALL_LOCATION
from k3s_slack.utils import get_logger

LOGGER = get_logger(__name__)


def print_help(say):
    say(("Available commands:\n"
         "help - Prints this help\n"
         "self-update - Bot updates itself\n"
         "check-updates - Prints currently running versions and if there is an update"))


def self_update(say):
    if os.geteuid() != 0 or not os.path.isdir(INSTALL_LOCATION):
        say(f"Bot is not running as a service, unable to self-update")


def check_updates(say):
    latest_version = "unknown"
    r = requests.get(VERSION_CHECK_URL)
    if r.status_code == 200:
        for line in r.text.splitlines():
            if line.startswith("VERSION"):
                latest_version = line.split("=")[1].strip().strip('"')
                break

    if VERSION == latest_version:
        say(f"I'm running k3s-slack-bot version *{VERSION}*, this is the latest version")
    else:
        say(f"I'm running k3s-slack-bot version *{VERSION}*, latest is *{latest_version}*")
