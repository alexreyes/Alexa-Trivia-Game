# Alexa-Trivia-Game
A simple trivia game made using flask ask for the Amazon Echo/dot

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
