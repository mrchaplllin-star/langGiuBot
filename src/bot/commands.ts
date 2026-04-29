import type { Context, Telegraf } from 'telegraf';

import type { AppConfig } from '../config.js';
import { postMessageToChannel } from './handlers.js';

const COMMAND_LIST = [
  '/start - Welcome and command list',
  '/help - What this bot can do',
  '/settings - Bot preferences (placeholder)',
  '/talk - Start conversation mode (placeholder)',
  '/finish - Finish session (placeholder)',
  '/dictionary - Export dictionary (placeholder)',
  '/words - Show vocabulary stats (placeholder)',
  '/posttest - Test posting to channel',
].join('\n');

export function registerCommands(bot: Telegraf<Context>, config: AppConfig): void {
  bot.start(async (ctx) => {
    await ctx.reply(
      `Welcome to your Italian Learning Assistant starter!\n\nAvailable commands:\n${COMMAND_LIST}`,
    );
  });

  bot.command('help', async (ctx) => {
    await ctx.reply(
      'This bot is the foundation of a future Italian learning assistant. ' +
        'For now, it supports basic commands and Telegram channel posting tests.',
    );
  });

  bot.command('settings', async (ctx) => {
    await ctx.reply('Settings are not implemented yet.');
  });

  bot.command('talk', async (ctx) => {
    await ctx.reply('Conversation mode will be added next.');
  });

  bot.command('finish', async (ctx) => {
    await ctx.reply('Session analysis will be added next.');
  });

  bot.command('dictionary', async (ctx) => {
    await ctx.reply('Dictionary export will be added next.');
  });

  bot.command('words', async (ctx) => {
    await ctx.reply('Vocabulary stats will be added next.');
  });

  bot.command('posttest', async (ctx) => {
    await ctx.reply('Trying to post a test message to the configured channel...');

    await postMessageToChannel(bot, config.telegramChannelId, 'Test post from bot');

    await ctx.reply('Test message posted successfully.');
  });
}
