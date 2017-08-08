
# from random import randint

# from flask import Flask, render_template

# from flask_ask import Ask, statement, question, session


# app = Flask(__name__)

# ask = Ask(app, "/")

# logging.getLogger("flask_ask").setLevel(logging.DEBUG)


# def makeAPICall():

#     r = requests.get("https://opentdb.com/api.php?amount=1")

#     if r.status_code != 200:
#         # This means something went wrong.
#         raise ApiError('GET /tasks/ {}'.format(r.status_code))

#     data = r.json()
    
#     theQuestion = "" +  data["results"][0]["question"]
#     theCorrectAnswer = data["results"][0]["correct_answer"]

#     return ("" + theQuestion + ". Answer: " + theCorrectAnswer)    

# def getBoolean():
#     r = requests.get("https://opentdb.com/api.php?amount=1")

#     if r.status_code != 200:
#         # This means something went wrong.
#         raise ApiError('GET /tasks/ {}'.format(r.status_code))

#     data = r.json()
    
#     theType = data["results"][0]["type"]
#     print (theType)

#     return (theType)

# @ask.launch

# def new_game():

#     #welcome: Welcome to memory game. I'm going to say three numbers for you to repeat backwards. Ready?
#     welcome_msg = render_template('welcome')

#     return (question(welcome_msg))


# @ask.intent("YesIntent")

# def next_round():

#     myQuestion = "" + makeAPICall()
#     getBooleanReturn = getBoolean()
    
#     #round: Can you repeat the numbers {{ numbers|join(", ") }} backwards?
    
#     if (getBooleanReturn == 'boolean'):
#         round_msg = render_template('boolean', myQuestion = myQuestion)

#     else: 
#         round_msg = render_template('round', myQuestion = myQuestion)

#     print(myQuestion)

#     session.attributes['theQuestion'] = myQuestion

#     return question(round_msg)

# @ask.intent("AnswerIntent", convert={'guess': str})

# def answer(guess):

#     winning_numbers = session.attributes['theQuestion']

#     if guess.lower() == winning_numbers:

#         msg = render_template('win')

#     else:
#         print ("Expected value" + winning_numbers + ". Received: " + guess)
#         msg = render_template('lose', answer = answer)

#     return statement(msg)

# if __name__ == '__main__':

#     app.run(debug=True)

import logging

import requests

import json

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)

def makeAPICall():

    r = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy")

    if r.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(r.status_code))

    data = r.json()
    
    theQuestion = "" +  data["results"][0]["question"]
    theCorrectAnswer = data["results"][0]["correct_answer"]
    theType = data["results"][0]["type"]

    session.attributes['the_type'] = theType
    session.attributes['correct_answer'] = theCorrectAnswer

    return ("" + theQuestion)

@ask.intent("YesIntent")

def next_round():
    myQuestion = makeAPICall()
    the_type = session.attributes['the_type']

    if (the_type == 'boolean'):
        msg = render_template('roundBoolean', myQuestion = myQuestion)
    else:
        msg = render_template('round', myQuestion=myQuestion)

    session.attributes['question'] = myQuestion

    return question(msg)


@ask.intent("AnswerIntent", convert={'first': str})

def answer(first):

    correct_answer = session.attributes['correct_answer']
    the_type = session.attributes['the_type']
    myQuestion = correct_answer

    print(first)
    print(correct_answer)
    print(the_type)

    if first.lower() == correct_answer.lower():

        msg = render_template('win')

    else:
        msg = render_template('lose', myQuestion=myQuestion)

    return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)