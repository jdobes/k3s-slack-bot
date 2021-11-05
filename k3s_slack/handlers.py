import os
import tempfile

import requests

import k3s_slack.config as CFG
from k3s_slack.utils import get_logger, run_command, ensure_latest_git_repo

LOGGER = get_logger(__name__)


def _get_latest_bot_version():
    latest_version = "unknown"
    ensure_latest_git_repo(CFG.BOT_GH_REPO, CFG.BOT_GH_REPO_NAME)
    with open(f"/tmp/{CFG.BOT_GH_REPO_NAME}/{CFG.BOT_VERSION_CHECK_FILE}", "r") as fp:
        version_file_lines = fp.readlines()
    for line in version_file_lines:
        if line.startswith("VERSION"):
            latest_version = line.split("=")[1].strip().strip('"')
            break
    return latest_version


def print_help(say):
    say(("Available commands:\n"
         "help - Prints this help\n"
         "self-update - Bot updates itself\n"
         "k3s-update - K3s update\n"
         "check-updates - Prints currently running versions and if there is an update"))


def self_update(say=None, force=False):
    if os.geteuid() != 0 or not CFG.SERVICE_MODE:
        LOGGER.info("Bot is not running as a service, unable to self-update")
        if say:
            say(f"Bot is not running as a service, unable to self-update")
        return

    latest_version = _get_latest_bot_version()
    if CFG.VERSION == latest_version and not force:
        LOGGER.info("Bot is already running latest version")
        if say:
            say(f"Bot is already running latest version")
        return

    run_command(["bash", f"/tmp/{CFG.BOT_GH_REPO_NAME}/{CFG.BOT_INSTALLER_FILE}"],
                env={"SLACK_BOT_TOKEN": CFG.SLACK_BOT_TOKEN, "SLACK_APP_TOKEN": CFG.SLACK_APP_TOKEN})


def k3s_update(say):
    say("Starting k3s update")
    with tempfile.NamedTemporaryFile() as fp:
        r = requests.get(CFG.K3S_INSTALLER_URL)
        if r.status_code == 200:
            fp.write(r.content)
            fp.flush()
            run_command(["sh", fp.name])
    say("k3s update finished")


def check_updates(say):
    latest_version = _get_latest_bot_version()
    if CFG.VERSION == latest_version:
        say(f"I'm running k3s-slack-bot version *{CFG.VERSION}*, this is the latest version")
    else:
        say(f"I'm running k3s-slack-bot version *{CFG.VERSION}*, latest is *{latest_version}*")
