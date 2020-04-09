import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(message.author.name + ': ' + message.content)

        if (message.content == "it's a godawful small affair") or (message.content == "It's a godawful small affair"):
            await message.channel.send('To the girl with the mousy hair')

        if (message.content == 'but her mummy is yelling, "No!"') or (message.content == 'But her mummy is yelling, "No!"'):
            await message.channel.send('And her daddy has told her to go')

        if (message.content == 'But her friend is nowhere to be seen') or (message.content == 'but her friend is nowhere to be seen'):
            await message.channel.send('Now she walks through her sunken dream')

        if (message.content == 'To the seat with the clearest view') or (message.content == 'to the seat with the clearest view'):
            await message.channel.send("And she's hooked to the silver screen")

        if (message.content == 'But the film is a saddening bore') or (message.content == 'but the film is a saddening bore'):
            await message.channel.send("For she's lived it ten times or more")

        if (message.content == 'She could spit in the eyes of fools') or (message.content == 'she could spit in the eyes of fools'):
            await message.channel.send('As they ask her to focus on')

        if (message.content == 'Sailors fighting in the dance hall') or (message.content == 'sailors fighting in the dance hall'):
            await message.channel.send('Oh man!')

        if (message.content == 'Look at those cavemen go') or (message.content == 'look at those cavemen go'):
            await message.channel.send("It's the freakiest show")

        if (message.content == 'Take a look at the Lawman') or (message.content == 'take a look at the Lawman'):
            await message.channel.send('Beating up the wrong guy')

        if (message.content == "Oh man! Wonder if he'll ever know") or (message.content == "oh man! wonder if he'll ever know"):
            await message.channel.send("He's in the best selling show" + '\n' +"Is there life on Marrssssssss?")

        if (message.content == "It's on America's tortured brow") or (message.content == "it's on america's tortured brow"):
            await message.channel.send('That Mickey Mouse has grown up a cow')

        if (message.content == 'Now the workers have struck for fame') or (message.content == 'now the workers have struck for fame'):
            await message.channel.send("'Cause Lennon's on sale again")

        if (message.content == 'See the mice in their million hordes') or (message.content == 'see the mice in their million hordes'):
            await message.channel.send("From Ibiza to the Norfolk Broads")

        if (message.content == 'Rule Britannia is out of bounds') or (message.content == 'rule britannia is out of bounds'):
            await message.channel.send("To my mother, my dog, and clowns")

        if (message.content == "It's about to be writ again") or (message.content == "It's about to be writ again"):
            await message.channel.send("As I ask you to focus on")

        

        
            
        
        
        words = message.content.split()
        if message.author == self.user:
            return

        if words[0] == '!gottablast':
            await message.channel.send('https://us.rule34.xxx//images/1967/da76fa2c916ba40b972ef78fb949934c5984351a.gif')

        if words[0] == '!gimmesucc':
            await message.channel.send('https://us.rule34.xxx//images/1486/9e7b82d28b140edab8bd9e6558afe68a5a16acbf.gif')       

        if (words[0] == '!silence'):
            await message.channel.send('https://bit.ly/2RahTNY')

        if words[0] == '!say':
            toSend = ''
            toSend += '<@!' +str(message.author.id) + '> says: "'
            for i in range(1,len(words)):
                if(i == len(words)-1):
                    toSend = toSend + words[i] + '"'
                else:
                    toSend = toSend + words[i] + ' '
            await message.channel.send(toSend)

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(os.environ["Mari-Chan-Key"])
