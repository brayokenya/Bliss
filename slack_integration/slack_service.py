# slack_integration/slack_service.py

from slack_sdk import WebClient

slack_client = WebClient(token='xoxb-3129675285713-5860469874677-OCVhL1z83745rqL8fNGSqPvd')

def send_message(channel, text):
    response = slack_client.chat_postMessage(
        channel=channel,
        text=text
    )
    return response