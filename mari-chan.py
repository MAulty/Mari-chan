import discord
import os
import globals
import birthdays
import misc

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        globals.defChannel = discord.utils.get(client.get_all_channels(), guild__name='kitty kawk', name='kitty-quarantine')

    async def on_message(self, message):
        print(message.content)

        #Don't respond to ourselves
        words = message.content.split()
        if message.author == self.user:
            return

        #Command dispatching
        if len(words) > 0 and words[0] in globals.commands:
            await globals.commands[words[0]](words[1:], message)   

client = MyClient()
client.run(os.environ["Mari-Chan-Key"])
