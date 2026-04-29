import type { Context, Telegraf } from 'telegraf';
import { TelegramError } from 'telegraf';

import type { AppConfig } from '../config.js';
import { logger } from '../utils/logger.js';

export async function postMessageToChannel(
  bot: Telegraf<Context>,
  channelId: string,
  message: string,
): Promise<void> {
  try {
    await bot.telegram.sendMessage(channelId, message);
  } catch (error: unknown) {
    if (error instanceof TelegramError) {
      logger.error(`Telegram API error while posting to channel: ${error.description}`);
    } else {
      logger.error('Unknown error while posting to channel', error);
    }
    throw error;
  }
}

export function registerEventHandlers(bot: Telegraf<Context>, config: AppConfig): void {
  bot.catch((error: unknown, ctx) => {
    const updateType = ctx.updateType;

    if (error instanceof TelegramError) {
      logger.error(`Telegram API error on update [${updateType}]: ${error.description}`);
      return;
    }

    logger.error(`Unhandled bot error on update [${updateType}]`, error);
  });

  // Future place for non-command handlers (text, callback queries, etc.)
  // - OpenAI response generation can be plugged in here.
  // - Supabase read/write logic can be added in repository modules.
  bot.on('message', async (ctx, next) => {
    logger.info(`Incoming message from chat=${ctx.chat.id}`);
    await next();
  });

  logger.info(`Handlers registered (target channel: ${config.telegramChannelId})`);
}
