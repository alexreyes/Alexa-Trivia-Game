import requests
import json

r = requests.get("https://opentdb.com/api.php?amount=1")

if r.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(r.status_code))

data = r.json()

print data["results"][0]["category"]
print data["results"][0]["type"]
print data["results"][0]["difficulty"]
print data["results"][0]["question"]
print data["results"][0]["correct_answer"]
print data["results"][0]["incorrect_answers"]