import discord
import os
from datetime import date
from datetime import datetime, timedelta
from threading import Timer
import time
import globals
import praw

#Check daily for r/DankMemes hot posts
x = datetime.today()
y = x.replace(day=x.day, hour=7, minute=50) + timedelta(days=1)
seconds = (y - x).total_seconds()
t: Timer = None

async def RedditGrab():
    print('Starting reddit grab..')
    reddit = praw.Reddit(client_id=os.environ["praw_client_id"],
                         client_secret=os.environ["praw_client_secret"],
                         password=os.environ["praw_password"],
                         user_agent="linux:com.github.mari-chan-bot:a0.0.1 (by u/mari-chan-bot)",
                         username=os.environ["praw_username"])
    print('successful login...')
    print('initializing subreddit')
    subreddit = reddit.subreddit('dankmemes')
    print('recieved subreddit')
    print('sending posts')
    for submission in subreddit.hot(limit=5):
        if(submission.url.startswith("https://i.")):
            await globals.defMemeChannel.send(submission.url)


t = Timer(seconds, RedditGrab)
t.start()

#debugger off cunt
async def DebugMemes(params, message):
    await RedditGrab()
globals.commands.update({"!debug-memes": DebugMemes})
