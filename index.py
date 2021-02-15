from bottle import route, run, error, template
from dotenv import load_dotenv
import random, os, json, sys, requests

# Get our enviroment variables
load_dotenv()

# Global Variables
# Literally the devil
compliments = []
apiKey = os.getenv("APIKEY") # This is for unSplash if we ever get that working with our API key... Otherwise we can use source.unsplash I guess. I need to check the API TOS

# Lets load all the compliments in a way that we really should clean up.
# Seriously we need to clean this up. This is really disgusting and bloated
# Maybe a SQLite database? Or MongoDB? or MariaDB?
# Just anything other than loading from a .txt file when in deployment
# You know, memory usage reasons...
try:
    complimentFile = open("compliments.txt", "r")

    for line in complimentFile:
        # Clean up the text from the compliments file
        # TODO: Ensure there are no unicode errors slipping through
        line.strip()
        line.rstrip()

        # Add it to the global Compliments
        compliments.append(line)

    complimentFile.close()

except Exception as e:
    print("Something went wrong!")
    print(f"{e}")


def getRandomBackground():
    """
    getRandomBackground() -> String

    Usage: getRandomBackground(), returns a random string in the form of a URL from unsplash
    Assumes apiKey is a globally defined variable that it can reference through fStrings

    TODO:
    Clean this up to accept a APIKey as a paremeter instead of assumine globals exist
    """
    #imagePayload = requests.get(f"https://api.unsplash.com/photos/?client_id={apiKey}&per_page=1")
    #decodedPayload = json.loads(imagePayload.text)

    return("https://source.unsplash.com/1920x1080/?food")

def getRandomCompliment():
    """
        getRandomCompliment() -> String

        Usage: getRandomCompliment(), returns a random string from a global list named compliments
        Assumes a global list named compliments exists already and returns a random entry from list

        TODO:
        Clean this function up so it can pull random compliments from various sources. Also ensure it
        doesn't make broad sweeping assumptions about what may and may not exist in the program.

    """
    compliment = random.choice(compliments)
    compliment.rstrip()
    compliment.strip()
    return compliment

# This is the first page anyone will see when the click the link.
# KISS is the ideology followed here. Any serious logic is handeled in the template.
# Templates should be able to redefine themselves as they feel.
@route("/")
def provideIndexPage():
    return template("index.tpl", title="Compliments As A Service", compliment=getRandomCompliment(), backgroundImage=getRandomBackground())

# This is the actual API
# TODO: Document this.
@route("/compliment/")
@route("/compliment")
def provideCompliment():
    return getRandomCompliment()

# This is the actual JSON API
# TODO: Document this.
@route("/jsoncompliment/")
@route("/jsoncompliment")
def provideJSONCompliment():
    return json.dumps({"compliment" : getRandomCompliment()})

# The user tried to get to a nonexistent page. 404!
@error(404)
def error404(error):
    return("You're lost mate!: Bottle Error: {}".format(error))

# The user shattered bottle. Crap. Can someone get a broom and dustpan?!
@error(500)
def error500(error):
    return("You've upset Bottle male!: Bottle Error: {}".format(error))

run(host="localhost", port=int(os.getenv("port")), reloader=os.getenv("reloader"), debug=os.getenv("debugmode"))

print("Goodbye Friend!")
