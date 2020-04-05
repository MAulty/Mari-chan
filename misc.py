import discord
import globals

#!gimmesucc gives a succ gif
async def GimmeSuccCommand(params, message):
    message.channel.send('https://us.rule34.xxx//images/1486/9e7b82d28b140edab8bd9e6558afe68a5a16acbf.gif')
globals.commands.update({"!gimmesucc": GimmeSuccCommand})

#!echo repeats the text
async def EchoCommand(params, message):
    if params[0] is None:
        await message.channel.send('Nothing to echo')
    toSend = ""
    for i in params:
        toSend += i + " "
    await message.channel.send(toSend)
globals.commands.update({"!echo": EchoCommand})
