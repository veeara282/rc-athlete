"""
Adapted from https://github.com/letsdiscodev/example-flask-site/blob/main/server.py

Copyright (c) 2024 Antoine Leclair and Greg Sadetsky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import datetime, timezone

from flask import Flask
from jinja2 import Environment, FileSystemLoader, select_autoescape
import zulip

app = Flask(__name__)

jinja_env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = jinja_env.get_template("index.html.j2")

# No zuliprc - client is configured using environment variables via dashboard.disco.cloud
client = zulip.Client()


@app.route("/")
def index():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    # now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S")
    return template.render(now=now)


@app.route("/send-message", methods=["POST"])
def send_message():
    request = {
        "type": "channel",
        "to": "test-bot",
        "topic": "sports bot",
        "content": "Let's go Knicks!",
    }
    result = client.send_message(request)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
