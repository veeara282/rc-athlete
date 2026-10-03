"""cron job: runs every Monday at 13:00 UTC (9:00 am EDT or 8:00 am EST)
"""

from datetime import datetime, timezone

import zulip_utils

# No zuliprc - client is configured using environment variables via dashboard.disco.cloud
client = zulip_utils.get_client()


now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
zulip_utils.send_message(f"Hello, world! It is {now}")
