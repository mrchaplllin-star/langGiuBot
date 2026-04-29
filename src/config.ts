import dotenv from 'dotenv';

dotenv.config();

export type AppConfig = {
  telegramBotToken: string;
  telegramChannelId: string;
  port: number;
  nodeEnv: string;
};

function getRequiredEnv(name: string): string {
  const value = process.env[name];

  if (!value || value.trim() === '') {
    throw new Error(`Missing required environment variable: ${name}`);
  }

  return value;
}

export function loadConfig(): AppConfig {
  const telegramBotToken = getRequiredEnv('TELEGRAM_BOT_TOKEN');
  const telegramChannelId = getRequiredEnv('TELEGRAM_CHANNEL_ID');
  const nodeEnv = process.env.NODE_ENV?.trim() || 'development';

  const rawPort = process.env.PORT?.trim() || '3000';
  const port = Number(rawPort);

  if (Number.isNaN(port) || port <= 0) {
    throw new Error(`Invalid PORT value: ${rawPort}`);
  }

  return {
    telegramBotToken,
    telegramChannelId,
    port,
    nodeEnv,
  };
}
