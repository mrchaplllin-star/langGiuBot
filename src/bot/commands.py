from telegram import Update
from telegram.ext import ContextTypes

from src.bot.handlers import post_message_to_channel


def _command_list() -> str:
    return "\n".join(
        [
            "/start - Welcome and command list",
            "/help - What this bot can do",
            "/settings - Settings placeholder",
            "/talk - Conversation mode placeholder",
            "/finish - Session analysis placeholder",
            "/dictionary - Dictionary export placeholder",
            "/words - Vocabulary stats placeholder",
            "/posttest - Test posting to channel",
        ]
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to your Italian Learning Assistant starter!\n\n"
        f"Available commands:\n{_command_list()}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "This bot is the foundation of a future Italian learning assistant. "
        "For now, it supports basic commands and Telegram channel posting tests."
    )


async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Settings are not implemented yet")


async def talk_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Conversation mode will be added next")


async def finish_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Session analysis will be added next")


async def dictionary_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Dictionary export will be added next")


async def words_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Vocabulary stats will be added next")


async def posttest_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Trying to post a test message to the configured channel..."
    )
    channel_id = context.bot_data["telegram_channel_id"]
    await post_message_to_channel(context, channel_id, "Test post from bot")
    await update.message.reply_text("Test message posted successfully.")
