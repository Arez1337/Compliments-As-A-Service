from bottle import route, run, error
import random

# Global Variables",
# Literally the devil",
compliments = [
"Your smile is contagious",
"I bet you make babies smile",
"You have the best laugh",
"You light up the room",
"You have a great sense of humor",
"If cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now",
"You're like sunshine on a rainy day",
"You bring out the best in other people",
"I bet you sweat glitter",
"Colors seem brighter when you're around",
"You're more fun than a ball pit filled with candy",
"Jokes are funnier when you tell them",
"You always know how to find that silver lining",
"You're a candle in the darkness",
"Being around you is like a happy little vacation",
"You're more fun than bubble wrap",
"You're like a breath of fresh air",
"You're someone's reason to smile",
"How do you keep being so funny and making everyone laugh?"
]

@route('/app/<myid:int>/')
def provide(myid):
    return "Object with id {} returned".format(myid)

@route("/")
def indexPage():
    """"
    "This is where we can serve a generic page to a web browser explaining how to use the Compliment API", Its Compliments As A Service all the way down!
    """

    return("test")

@route('/compliment/<type>')
def provide(type):
    if type == "generic":
        return random.choice(compliments)

    elif type == "mytype":
        return ""

@error(404)
def error404(error):
    return("You're lost mate!: Bottle Error: {}".format(error))

@error(500)
def error500(error):
    return("You're lost mate!: Bottle Error: {}".format(error))

run(host='localhost', port=8080, debug=True, reloader=True)

print("Goodbye")
