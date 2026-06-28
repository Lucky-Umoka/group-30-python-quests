#!/usr/bin/python3
def personalized_greeting(name, quest):
    print(f"Greetings, {name}! Your task is: {quest}. Go on and good luck!")

name = input('What  is your name? ')
quest = input('Which level do you prefer? ')

personalized_greeting(name, quest)
