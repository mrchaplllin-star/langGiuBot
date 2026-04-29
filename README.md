# Telegram Bot Starter (Python, no compilation)

This is a production-ready Telegram bot starter for a future Italian learning assistant.

## Stack
- Python 3.11+
- python-telegram-bot
- python-dotenv

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment
```bash
cp .env.example .env
```
Set values in `.env`:
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHANNEL_ID`
- `PORT`
- `NODE_ENV`

## BotFather setup
1. Open Telegram and chat with `@BotFather`
2. Run `/newbot`
3. Save token into `TELEGRAM_BOT_TOKEN`
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
