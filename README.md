# Telegram Bot Starter (Python, no compilation)

This is a production-ready Telegram bot starter for a future Italian learning assistant.

## Stack
- Python 3.11+
- python-telegram-bot
- python-dotenv

## Install
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

## Environment
Copy and edit env file:
```bash
copy .env.example .env
```
(Use `cp .env.example .env` on macOS/Linux.)

Set values in `.env`:
- `TELEGRAM_BOT_TOKEN=...`
- `TELEGRAM_CHANNEL_ID=...`
- `PORT=3000`
- `NODE_ENV=development`

> Important: do **not** paste token directly into Python code. Keep it only in `.env`.

## BotFather setup
1. Open Telegram and chat with `@BotFather`
2. Run `/newbot`
3. Save token into `TELEGRAM_BOT_TOKEN` in `.env`
4. Optional: use `/setcommands` with:
   - start - Welcome and command list
   - help - What this bot can do
   - settings - Settings placeholder
   - talk - Conversation mode placeholder
   - finish - Session analysis placeholder
   - dictionary - Dictionary export placeholder
   - words - Vocabulary stats placeholder
   - posttest - Post test message to channel

## Add bot to channel
1. Open channel settings → Administrators
2. Add bot as admin
3. Allow posting messages
4. Put username/id into `TELEGRAM_CHANNEL_ID`

## Run locally
```bash
python -m src.index
```

## Troubleshooting (Windows)
If you see `Missing required environment variable: TELEGRAM_BOT_TOKEN`:
1. Ensure `.env` exists in project root (same folder as `README.md`).
2. Ensure line format is exactly `TELEGRAM_BOT_TOKEN=your_real_token`.
3. Restart terminal after editing `.env` (or deactivate/activate venv again).
4. Run again: `python -m src.index`.

If you see `Invalid _required(...) usage...`:
- You accidentally passed token text into `_required(...)` in code.
- Restore: `_required("TELEGRAM_BOT_TOKEN")`.

## Commands
- `/start`
- `/help`
- `/settings`
- `/talk`
- `/finish`
- `/dictionary`
- `/words`
- `/posttest`

`/posttest` posts: `Test post from bot` to configured channel.

## Structure
- `src/bot/` commands and handlers
- `src/config.py` env validation
- `src/utils/logger.py` logging
- `src/ai`, `src/db`, `src/reports`, `src/vocabulary` placeholders for future OpenAI/Supabase/features

No Docker, no database, no OpenAI yet.
