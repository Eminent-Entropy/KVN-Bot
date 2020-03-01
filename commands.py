import discord, asyncio
from discord.ext import commands

from bot import bot

class Commands():
	@bot.commands()
	async def ping(ctx):
		await ctx.send('pong')
	print('commands initialized')

