import pymongo
import discord
import globals

#Database setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Mari-Chan"]
movies = db["Movies"]
ratings = db["Ratings"]

#!add-movie <title> ~<watch-link> ~<imdb-link>
async def AddMovieCommand(params, message):
    imdbLink = ""
    watchLink = ""

    #Fill link strings based on optional inputs
    if len(params) == 2:
        if "imdb.com" in params[1]:
            imdbLink = params[1]
        else:
            watchLink = params[1]
    elif  len(params) == 3:
        imdbLink = params[1]
        watchLink = params[2]
    elif len(params) == 0:
        await message.channel.send("!add-movie <title> ~<watch-link> ~<imdb-link>")
        return

    #Insert new item
    movies.insert_one({
        "Title": params[0],
        "IMDB": imdbLink,
        "WatchLink": watchLink
    })

    #Show movie
    output = "Movie, " + params[0] + " added successfully!";
    if len(watchLink) > 0: output += "\nWatch at: " + watchLink
    if len(imdbLink) > 0: output += "\nSee IMDB: " + imdbLink
    await message.channel.send(output)
globals.commands.update({"!add-movie": AddMovieCommand})

#!add-movie-rating <title> <rating/10>
async def AddMovieRatingCommand(params, message):
    user = message.author.mention

    #Only allow 2 params
    if len(params) != 2:
        await message.channel.send("!add-movie-rating <title> <rating/10>")
        return

    #Check if movie exists
    if movies.find_one({"Title": params[0]}) == None:
        await message.channel.send("Could not find title: " + params[0])
        return

    #Make sure i have never rated this movie
    pastRating = ratings.find_one({"Movie": params[0], "UserRated": user})
    if pastRating != None:
        await message.channel.send("You already rated this movie a " + str(pastRating["Rating"]) + "!!!")
        return

    #Add rating
    ratings.insert_one({
        "Movie": params[0],
        "UserRated": user,
        "Rating": float(params[1])
    })

    #Respond
    await message.channel.send("Movie rating added successfully!")
globals.commands.update({"!add-movie-rating": AddMovieRatingCommand})

#show-movie <Movie>
async def ShowMovieCommand(params, message):
    #Get movie
    movie = movies.find_one({"Title": params[0]})
    if movie == None:
        await message.channel.send("Could not find movie...")
        return
    
    #Get ratings
    movieRatings = ratings.find({"Movie": params[0]})

    #Output
    out = "***" + movie["Title"] + "***\n"
    if movie["IMDB"] != "": out += "\n**IMDB**: " + movie["IMDB"]
    if movie["WatchLink"] != "": out += "\n**WatchLink**: " + movie["WatchLink"]

    if movieRatings.alive == True:
        out += "\n\n**Ratings**:"
        for rating in movieRatings:
            out += "\n> " + rating["UserRated"] + ": " + str(rating["Rating"])
    movieRatings.close()

    await message.channel.send(out)

globals.commands.update({"!show-movie": ShowMovieCommand})
