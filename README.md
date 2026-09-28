# rc-athlete
Bot that posts sports updates to a Zulip channel

## Architecture notes

- Sports data source: [TheSportsDB Free Sports API](https://www.thesportsdb.com/documentation)
  - Use free API key `123`
  - Get sports team info:
    ```bash
    curl -L https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=yankees | jq "." | less
    ```
  - Get upcoming events for a sports team:
    ```bash
    # New York Yankees: 135260
    curl -L https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=135260 | jq "." | less
    # New York Mets: 135275
    curl -L https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=135275 | jq "." | less
    ```
- Post messages to Zulip: https://recurse.zulipchat.com/api/send-message
  - Zulip recommends putting config in a `.zuliprc` file
