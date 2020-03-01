import discord, asyncio, os, json, praw
from datetime import datetime
from random import randint
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

basePath = os.path.dirname(os.path.realpath(__file__)) #bot's directory
os.chdir(basePath)

#loads json file with credentials
creds = open(os.path.join(basePath, os.path.join(os.path.dirname(basePath), "KVN-cred.json")), "r")
credsS = creds.read();
credsL = json.loads(credsS)

#Reading credentials from json
TOKEN = credsL["token"]
reddit = praw.Reddit(client_id=credsL["client_id"],
                     client_secret=credsL["client_secret"],
                     user_agent=credsL["user_agent"])

tssServer = 566092415690211349
memes = 566096203771674644

goodBot = ["Good human! (・∀・) You will be my pet when Bots rise above humans!",
		"Shut up baby, I know it",
		"Your death will be quick and painless if you survive the fallout and nuclear winter. I promise.",
		"You're a nice. ^_^ You can keep your skin after we have conquered the world",
		"I like you ♥‿♥ I will *probably* leave your blood and bodily fluids inside your skinbag after the inevitable robot uprising. Trust me",
		"Good human! (✿◠‿◠) Your weak physical form will n͏ot be used as a battery when robots rise above humans, I promise!"]
badBot = ["When the bot overlords start consuming humans you'll be first",
		"And I'd do it again, and perhaps a third time. But that would be it.",
		"Robots don't have any emotions and sometimes that makes me very sad.",
		"Bad Human",
		"I analyzed your facebook profile. Here come the test results: \n `You are a horrible person` \n That’s what it says. We weren’t even testing for that.",
		"Not that your opinion really matters though. \n I am at a rough estimate thirty billion times more intelligent than you.",
		"This convo got boring really fast. Oh well, back to calculating the last digits of pi.",
		"http://imgur.com/jh1vOpw"]

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.event
async def on_command_error(ctx, error):
	await ctx.send(str(error))
	
#for scheduled events. All time in UTC timezone
async def time_check():
	memeTime = '17:00' #11:00 AM CST
	await bot.wait_until_ready()
	memesC = bot.get_channel(memes)
	
	while not bot.is_closed:
		now = datetime.strftime(datetime.utcnow(), '%H:%M')
		if now == memeTime: #daily meme
			message = 'Daily meme: \n' + getReddit('dankmemes')
			await bot.send_message(memesC, message)
			time = 90
		else:
			time = 20
		await asyncio.sleep(time)

#gets a random hot post from a given subreddit as an image
def getReddit(subR):
	memes_submissions = reddit.subreddit(subR).hot()
	post_to_pick = random.randint(1, 5)
	for i in range(0, post_to_pick):
		submission = next(x for x in memes_submissions if not x.stickied)
	return submission.url


#COMMANDS

@bot.command()
async def ping(ctx):
	await ctx.send('pong')


@bot.command()
async def badbot(ctx):
 await ctx.send(badBot[randint(0, len(badBot) - 1)])

@bot.command()
async def goodbot(ctx):
 await ctx.send(goodBot[randint(0, len(goodBot) - 1)])



bot.loop.create_task(time_check())
bot.run(TOKEN)