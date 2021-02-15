from bottle import route, run, error, template
from dotenv import load_dotenv
import random, os, json, sys, requests

# Get our enviroment variables
load_dotenv()

# Global Variables
# Literally the devil
compliments = []
apiKey = os.getenv("APIKEY")

# Lets load all the compliments in a way that we really should clean up.
try:
    complimentFile = open("compliments.txt", "r")

    for line in complimentFile:
        # Clean up the text from the compliments file
        line.strip()
        line.rstrip()

        # Add it to the global Compliments
        compliments.append(line)

    complimentFile.close()

except Exception as e:
    print("Something went wrong!")
    print(f"{e}")

def getRandomBackground():
    imagePayload = requests.get(f"https://api.unsplash.com/photos/?client_id={apiKey}&per_page=1")
    decodedPayload = json.loads(imagePayload.text)

    return("https://source.unsplash.com/1920x1080/?nature")

def getRandomCompliment():
    compliment = random.choice(compliments)
    compliment.rstrip()
    compliment.strip()
    return compliment

@route("/")
def provideIndexPage():
    """"
    This is where we can serve a generic page to a web browser explaining how to use the Compliment API",
    Its Compliments As A Service all the way down!
    """
    return("Welcome to the Compliments As A Service API. Simply make a empty GET request to /compliment/ to get a compliment returned as a string!")

@route("/compliment/")
@route("/compliment")
def provideCompliment():
    return getRandomCompliment()

@route("/jsoncompliment/")
@route("/jsoncompliment")
def provideJSONCompliment():
    return json.dumps({"compliment" : getRandomCompliment()})

@route("/templatetest")
def templateTest():
    return template("index.tpl", title="Compliments As A Service", compliment=getRandomCompliment(), backgroundImage=getRandomBackground())

# Self Explaintory
@error(404)
def error404(error):
    return("You're lost mate!: Bottle Error: {}".format(error))

# Self Explaintory
@error(500)
def error500(error):
    return("You've upset Bottle male!: Bottle Error: {}".format(error))

run(host="localhost", port=8080, reloader=True, debug=True)

print("Goodbye, friend...")
