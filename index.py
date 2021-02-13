from bottle import route, run, error
import random, os, json, sys

# Global Variables
# Literally the devil
compliments = []

try:
    complimentFile = open("compliments.txt", "r")

    for line in complimentFile:
        # Clean up the text from the compliments file
        line.strip()
        line.rstrip()

        # Add it to the global Compliments
        compliments.append(line)

except Exception as e:
    print("Something went wrong!")
    print(f"{e}")


@route("/")
def indexPage():
    """"
    This is where we can serve a generic page to a web browser explaining how to use the Compliment API", Its Compliments As A Service all the way down!
    """
    return("Welcome to the Compliments As A Service API. Simply make a empty GET request to /compliment/generic/ to get a compliment returned as a string!")

@route('/compliment/<type>')
def provide(type):
    # Generic compliments.
    if type == "generic":
        return random.choice(compliments)
    # We will add compliment types all the time

# Self Explaintory
@error(404)
def error404(error):
    return("You're lost mate!: Bottle Error: {}".format(error))

# Self Explaintory
@error(500)
def error500(error):
    return("You've upset Bottle male!: Bottle Error: {}".format(error))

run(host='localhost', port=8080, debug=True, reloader=True)

print("Goodbye, friend...")
