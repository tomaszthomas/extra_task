import requests
import json

command = input("Write 'next' if you want to see the next joke: ")

while command != 'q':
    if command == 'next':
        joke = requests.get('http://api.icndb.com/jokes/random')
        joke_json = joke.json()
        print(joke_json['value']['joke'])
        command = input("Write 'next' if you want to see the next joke: ")
    else:
        break



