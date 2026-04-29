from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AppConfig:
    telegram_bot_token: str
    telegram_channel_id: str
    port: int
    node_env: str


def _required(env_name: str) -> str:
    """Return required env variable value with beginner-friendly validation."""
    # Guard against accidental code edits like _required("12345:ABC...")
    if ":" in env_name or env_name.startswith("-"):
        raise ValueError(
            "Invalid _required(...) usage. Pass environment variable name, "
            "not the token value. Example: _required('TELEGRAM_BOT_TOKEN')."
        )

    value = os.getenv(env_name, "").strip()
    if not value:
        raise ValueError(
            f"Missing required environment variable: {env_name}. "
            "Create .env from .env.example and set all required values."
        )
    return value


def load_config() -> AppConfig:
    token = _required("TELEGRAM_BOT_TOKEN")
    channel = _required("TELEGRAM_CHANNEL_ID")
    node_env = os.getenv("NODE_ENV", "development").strip() or "development"
    raw_port = os.getenv("PORT", "3000").strip()

    try:
        port = int(raw_port)
        if port <= 0:
            raise ValueError
    except ValueError as exc:
        raise ValueError(f"Invalid PORT value: {raw_port}") from exc

    return AppConfig(token, channel, port, node_env)
