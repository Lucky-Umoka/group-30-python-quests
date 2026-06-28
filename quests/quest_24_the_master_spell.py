#!/usr/bin/python3
def ask_for_age():
    age = int(input('Please enter your age: '))
    return age

def can_they_vote(age):
    if age >= 18:
        print(f"At {age} years old, you are eligible to vote!")
    else:
        print(f"At {age} years old, you are not eligible to vote. You have {18 - age} more year(s) to go.")

