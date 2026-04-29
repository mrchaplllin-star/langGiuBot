from telegram import Update
from telegram.ext import ContextTypes
from telegram.error import TelegramError

from src.utils.logger import setup_logger

logger = setup_logger()


async def post_message_to_channel(
    context: ContextTypes.DEFAULT_TYPE, channel_id: str, message: str
) -> None:
    try:
        await context.bot.send_message(chat_id=channel_id, text=message)
    except TelegramError as exc:
        logger.error("Telegram API error while posting to channel: %s", exc)
        raise


async def global_error_handler(
    update: object, context: ContextTypes.DEFAULT_TYPE
) -> None:
    logger.error("Unhandled exception: %s", context.error)
    if isinstance(update, Update) and update.effective_chat:
        try:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Something went wrong. Please try again later.",
            )
        except TelegramError as exc:
            logger.error("Failed to send error message to user: %s", exc)

    # Future integration point:
    # - OpenAI request/response orchestration hooks.
    # - Supabase persistence/retrieval hooks.
