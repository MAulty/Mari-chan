import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(message.content)
        words = message.content.split()
        if message.author == self.user:
            return

        if words[0] == '!gimmesucc':
            await message.channel.send('https://us.rule34.xxx//images/1486/9e7b82d28b140edab8bd9e6558afe68a5a16acbf.gif')       

        if words[0] == '!echo':
            if words[1] is None:
                await message.channel.send('Nothing to echo')
            toSend = ''
            for i in range(1,len(words)):
                toSend = toSend + words[i] + ' '
            await message.channel.send(toSend)

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(os.environ["Mari-Chan-Key"])
