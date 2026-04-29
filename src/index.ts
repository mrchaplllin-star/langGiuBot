import { Telegraf } from 'telegraf';

import { registerCommands } from './bot/commands.js';
import { registerEventHandlers } from './bot/handlers.js';
import { loadConfig } from './config.js';
import { logger } from './utils/logger.js';

function setupGracefulShutdown(bot: Telegraf, signals: NodeJS.Signals[]): void {
  signals.forEach((signal) => {
    process.once(signal, async () => {
      logger.warn(`Received ${signal}, shutting down gracefully...`);
      try {
        await bot.stop(signal);
      } finally {
        process.exit(0);
      }
    });
  });
}

async function bootstrap(): Promise<void> {
  try {
    const config = loadConfig();
    const bot = new Telegraf(config.telegramBotToken);

    registerEventHandlers(bot, config);
    registerCommands(bot, config);

    await bot.telegram.setMyCommands([
      { command: 'start', description: 'Welcome and command list' },
      { command: 'help', description: 'What the bot can do' },
      { command: 'settings', description: 'Settings placeholder' },
      { command: 'talk', description: 'Conversation mode placeholder' },
      { command: 'finish', description: 'Session analysis placeholder' },
      { command: 'dictionary', description: 'Dictionary export placeholder' },
      { command: 'words', description: 'Vocabulary stats placeholder' },
      { command: 'posttest', description: 'Post test message to channel' },
    ]);

    await bot.launch();
    logger.info(`Bot is running in ${config.nodeEnv} mode on port ${config.port}`);

    setupGracefulShutdown(bot, ['SIGINT', 'SIGTERM']);
  } catch (error: unknown) {
    logger.error('Fatal startup error', error);
    process.exit(1);
  }
}

void bootstrap();
