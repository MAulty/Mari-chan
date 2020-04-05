import jsonpickle
from os import path
from datetime import date
from datetime import datetime
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
        if d.birthdate == date.today():
            return d
    return 0

#add-birthday event
async def AddBirthdayCommand(params, message):
    AddBirthday(params[0], params[1], datetime.strptime(params[2], "%Y/%m/%d").date())
    await message.channel.send("Birthday added!")
    SaveBirthdays()
globals.commands.update({"!add-birthday": AddBirthdayCommand})
