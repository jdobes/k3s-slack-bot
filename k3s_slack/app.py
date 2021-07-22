from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from k3s_slack.handlers import print_help, self_update, check_updates
from k3s_slack.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from k3s_slack.utils import init_logging

init_logging()
app = App(token=SLACK_BOT_TOKEN)


@app.message("help")
def handle_message_help(say):
    print_help(say)


@app.message("self-update")
def handle_message_help(say):
    self_update(say)


@app.message("check-updates")
def handle_message_help(say):
    check_updates(say)


@app.event("message")
def handle_message_events():
    pass


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
