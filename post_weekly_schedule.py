from datetime import datetime, timezone

import zulip_utils

# No zuliprc - client is configured using environment variables via dashboard.disco.cloud
client = zulip_utils.get_client()


now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
zulip_utils.send_message("Hello, world! It is {now}")
