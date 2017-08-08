# Alexa-Trivia-Game
A simple trivia game made using flask-ask for the Amazon Echo/dot. Basically the way it works is it just makes an API call to [openTDB](https://opentdb.com/api_config.php)

# Intent Schema/ Sample Utterances:
```
Intent Schema: 

{
  "intents": [
    {
      "intent": "YesIntent"
    },
    {
      "slots": [
        {
          "name": "first",
          "type": "RESPONSES"
        },
        {
          "name": "second",
          "type": "RESPONSES"
        }
      ],
      "intent": "AnswerIntent"
    }
  ]
}

Sample Utterances: 

YesIntent yeah
YesIntent yes
YesIntent sure
AnswerIntent {first}
```
