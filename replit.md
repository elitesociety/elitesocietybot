# elitesocietybot

A Telegram bot that greets users with a welcome image and delivers mission videos via inline keyboard buttons.

## Stack
- **Python 3.12**
- **python-telegram-bot 21.6** — Telegram bot framework
- **Flask** — keep-alive web server (port 8080, for UptimeRobot pings)

## How to run
The workflow `Start application` runs `python main.py`.

- The bot polls Telegram for updates
- A Flask server starts on port 8080 to keep the repl alive

## Required secrets
| Secret | Description |
|--------|-------------|
| `BOT_TOKEN` | Telegram bot token from @BotFather |

## Files
- `main.py` — bot logic (`/start` command, mission video handler)
- `keep_alive.py` — Flask keep-alive server
- `Welcome.jpg` — welcome image sent on `/start`
- `mission1.mp4` — mission video sent when user clicks START MISSION
