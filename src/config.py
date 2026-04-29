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


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
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
