import jsonpickle
from os import path
from datetime import date
from datetime import datetime, timedelta
from threading import Timer
import time
import discord
import globals

class Birthday:
    def __init__(self, name, uid, birthdate):
        self.name = name
        self.uid = uid
        self.birthdate = birthdate

#Properties
birthdays = []
bdayPath = "Birthdays.json"

#Birthday checking event once a day at 8am
x = datetime.today()
y = x.replace(day=x.day, hour=8, minute=0) + timedelta(days=1)
seconds = (y - x).total_seconds()
t: Timer = None
async def BirthdayCheck():
    print("checking")
    bday = CheckForBirthday()
    print(bday)
    if bday != None:
        print("sending")
        await globals.defChannel.send("Happy birthday " + bday.uid + "!!!")
t = Timer(seconds, BirthdayCheck)
t.start()

#Load from birthdays.json at start
if path.exists(bdayPath):
    with open(bdayPath) as infile:
        content = infile.read()
        birthdays = jsonpickle.decode(content)

#Save birthdays to file
def SaveBirthdays():
    with open(bdayPath, "w") as outfile:
        outfile.write(jsonpickle.encode(birthdays))

#Add a birthday
def AddBirthday(name, uid, birthdate):
    birthdays.append(Birthday(name, uid, birthdate))

#Checks each birthday for a match, returns Birthday if matches
def CheckForBirthday():
    for d in birthdays:
        today = date.today()
        bd = d.birthdate
        if bd.month == today.month and bd.day == today.day:
            print("found")
            return d
    return None

#!add-birthday event
async def AddBirthdayCommand(params, message):
    try:
        AddBirthday(params[0], params[1], datetime.strptime(params[2], "%Y/%m/%d").date())
        await message.channel.send("Birthday added!")
        SaveBirthdays()
    except:
        await message.channel.send("Birthday format: \n\t!add-birthday <Name> <User ping> <YYYY/MM/DD")
globals.commands.update({"!add-birthday": AddBirthdayCommand})

#!debug-check-bday
async def DebugCheckBdayCommand(params, message):
    print("message recieved")
    await BirthdayCheck()
globals.commands.update({"!debug-check-bday": DebugCheckBdayCommand})
