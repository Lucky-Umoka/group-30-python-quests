#!/usr/bin/env python3

print("Welcome to Sia's Social Media FizzBuzz!")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("YouTube")
    elif number % 3 == 0:
        print("Snapchat")
    elif number % 5 == 0:
        print("TikTok")
    else:
        print(number)

