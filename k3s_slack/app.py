from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import k3s_slack.config as CFG
from k3s_slack.handlers import print_help, self_update, check_updates
from k3s_slack.utils import init_logging, get_logger

init_logging()
app = App(token=CFG.SLACK_BOT_TOKEN)

LOGGER = get_logger(__name__)


@app.message("help")
def handle_message_help(say):
    print_help(say)


@app.message("self-update")
def handle_message_help(say):
    LOGGER.info("Self-update requested")
    self_update(say=say, force=True)


@app.message("check-updates")
def handle_message_help(say):
    check_updates(say)


@app.event("message")
def handle_message_events(message):
    if message["channel"] == CFG.GITHUB_UPDATES_CHANNEL_ID:
        for attachement in message.get("attachments", []):
            if CFG.BOT_GH_REPO in attachement["text"]:
                git_ref = attachement["text"].split("commit/")[1].split("|")[0]
                LOGGER.info(f"Bot repo update, git_ref={git_ref}, running self-update")
                self_update(force=False, git_ref=git_ref)
                break


if __name__ == "__main__":
    SocketModeHandler(app, CFG.SLACK_APP_TOKEN).start()
