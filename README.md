# Telegram Bot Starter (Node.js + TypeScript)

A production-ready starter for a Telegram bot that will later evolve into an Italian learning assistant.

## Tech Stack

- Node.js 20+
- TypeScript
- [Telegraf](https://telegraf.js.org/)

## Project Structure

```text
src/
  ai/           # Future OpenAI integration module
  bot/
    commands.ts # Command registration
    handlers.ts # Shared handlers and channel posting utility
  db/           # Future Supabase/database integration module
  reports/      # Future reporting/session analysis module
  utils/
    logger.ts   # Simple structured logger
  vocabulary/   # Future vocabulary storage/statistics module
  config.ts     # Environment variable loading + validation
  index.ts      # App entry point
```

## Environment Variables

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=@your_channel_username_or_numeric_id
PORT=3000
NODE_ENV=development
```

You can copy `.env.example`:

```bash
cp .env.example .env
```

## Install Dependencies

```bash
npm install
```

## Create the Bot with BotFather

1. Open Telegram and search for **@BotFather**.
2. Run `/newbot`.
3. Choose a display name and username (must end with `bot`).
4. Copy the generated token and set it in `TELEGRAM_BOT_TOKEN`.

## Get and Set Bot Token

- Token is provided by BotFather after `/newbot`.
- If needed, run `/token` in BotFather to regenerate it.
- Keep this token private.

## Set Commands in BotFather (optional but recommended)

You can set command hints manually with `/setcommands` in BotFather.
Use this list:

```text
start - Welcome and command list
help - What this bot can do
settings - Settings placeholder
talk - Conversation mode placeholder
finish - Session analysis placeholder
dictionary - Dictionary export placeholder
words - Vocabulary stats placeholder
posttest - Post test message to channel
```

> Note: The app also calls `setMyCommands` automatically on startup.

## Add Bot to a Telegram Channel as Admin

1. Create a channel (or open an existing one).
2. Open channel settings → Administrators.
3. Add your bot as an admin.
4. Grant permission to post messages.
5. Set `TELEGRAM_CHANNEL_ID` to either:
   - the channel username (e.g. `@my_channel`), or
   - numeric channel id (e.g. `-1001234567890`).

## Run Locally

Development mode:

```bash
npm run dev
```

Build and run production-like mode:

```bash
npm run build
npm start
```

## Available Commands

- `/start` – welcome + available commands
- `/help` – short explanation
- `/settings` – placeholder
- `/talk` – placeholder
- `/finish` – placeholder
- `/dictionary` – placeholder
- `/words` – placeholder
- `/posttest` – attempts to post `Test post from bot` in your configured channel

## Test `/posttest`

1. Make sure `TELEGRAM_CHANNEL_ID` is correct.
2. Make sure the bot is a channel admin with posting rights.
3. In private chat with your bot, send `/posttest`.
4. Confirm the message appears in your channel.

## Error Handling and Shutdown

- Required env vars are validated at startup.
- Telegram API errors are caught and logged with context.
- Unknown runtime errors are logged.
- Graceful shutdown is handled for `SIGINT` and `SIGTERM`.

## Future Integration Notes

- `src/ai/` is reserved for OpenAI integration.
- `src/db/` is reserved for Supabase logic.
- `src/reports/` and `src/vocabulary/` are placeholders for upcoming features.

No Docker, database, OpenAI, or external workflow integrations are included in this first version.
