from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import k3s_slack.config as CFG
from k3s_slack.handlers import print_help, self_update, k3s_update, check_updates
from k3s_slack.utils import init_logging, get_logger

init_logging()
app = App(token=CFG.SLACK_BOT_TOKEN)

LOGGER = get_logger(__name__)


@app.message("help")
def handle_message_help(say):
    print_help(say)


@app.message("self-update")
def handle_message_self_update(say):
    LOGGER.info("Self-update requested")
    self_update(say=say, force=True)


@app.message("k3s-update")
def handle_message_k3s_update(say):
    LOGGER.info("K3s-update requested")
    k3s_update(say)


@app.message("check-updates")
def handle_message_check_updates(say):
    check_updates(say)


@app.event("message")
def handle_message_events(message):
    if message["channel"] == CFG.GITHUB_UPDATES_CHANNEL_ID:
        for attachement in message.get("attachments", []):
            if CFG.BOT_GH_REPO_NAME in attachement["text"]:
                LOGGER.info(f"Bot repo update, running self-update")
                self_update(force=False)
                break


if __name__ == "__main__":
    SocketModeHandler(app, CFG.SLACK_APP_TOKEN).start()
