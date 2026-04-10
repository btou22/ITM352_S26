# Write a program to read the JSON file print it.

import json

filename = "quiz_data.json"

with open(filename) as file_object:
    quiz_data = json.load(file_object)
    print(quiz_data)