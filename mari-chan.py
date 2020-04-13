import discord
import os
import globals
import birthdays
import misc
import movies
import redditgrab

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        globals.defChannel = discord.utils.get(client.get_all_channels(), guild__name='kitty kawk', name='kitty-quarantine')
        globals.defMemeChannel = discord.utils.get(client.get_all_channels(), guild__name='kitty kawk', name='kitty-memes')

    async def on_message(self, message):
        #Don't respond to ourselves
        if message.author == self.user:
            return

        #Command dispatching
        params = SplitParams(message.content)
        if len(params) > 0 and params[0] in globals.commands:
            await globals.commands[params[0]](params[1:], message)

def SplitParams(str):
    params = [""]
    inQuote = False

    #Iterate through string
    for c in str:
        #Process differently if in ""
        if inQuote == False:
            #Split on space else set quote on quote else add character to latest param
            if c == ' ' and len(params[-1]) > 0:
                params.append("")
            elif c == '"':
                inQuote = True
            else:
                params[-1] += c
        else:
            #End quote part if ending quote else just add character
            if c == '"':
                inQuote = False
            else:
                params[-1] += c
    return params

client = MyClient()
client.run(os.environ["MARI_CHAN_KEY"])
