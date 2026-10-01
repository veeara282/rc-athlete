import zulip

global_client = zulip.Client()


def get_client():
    return global_client


def send_message(body, channel="test-bot", topic="sports bot", client=global_client):
    request = {
        "type": "channel",
        "to": channel,
        "topic": topic,
        "content": body,
    }
    result = client.send_message(request)
    return result
