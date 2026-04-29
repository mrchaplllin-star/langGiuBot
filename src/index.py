from telegram import BotCommand
from telegram.ext import Application, CommandHandler

from src.bot.commands import (
    dictionary_command,
    finish_command,
    help_command,
    posttest_command,
    settings_command,
    start_command,
    talk_command,
    words_command,
)
from src.bot.handlers import global_error_handler
from src.config import load_config
from src.utils.logger import setup_logger

logger = setup_logger()


def build_application() -> Application:
    config = load_config()
    app = Application.builder().token(config.telegram_bot_token).build()
    app.bot_data["telegram_channel_id"] = config.telegram_channel_id

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("settings", settings_command))
    app.add_handler(CommandHandler("talk", talk_command))
    app.add_handler(CommandHandler("finish", finish_command))
    app.add_handler(CommandHandler("dictionary", dictionary_command))
    app.add_handler(CommandHandler("words", words_command))
    app.add_handler(CommandHandler("posttest", posttest_command))

    app.add_error_handler(global_error_handler)
    return app


async def _set_commands(app: Application) -> None:
    await app.bot.set_my_commands(
        [
            BotCommand("start", "Welcome and command list"),
            BotCommand("help", "What the bot can do"),
            BotCommand("settings", "Settings placeholder"),
            BotCommand("talk", "Conversation mode placeholder"),
            BotCommand("finish", "Session analysis placeholder"),
            BotCommand("dictionary", "Dictionary export placeholder"),
            BotCommand("words", "Vocabulary stats placeholder"),
            BotCommand("posttest", "Post test message to channel"),
        ]
    )


def main() -> None:
    app = build_application()
    app.post_init = _set_commands
    logger.info("Starting bot with polling...")
    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
