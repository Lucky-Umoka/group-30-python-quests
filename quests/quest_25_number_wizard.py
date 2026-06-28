#!/usr/bin/env python3

secret_number = 32
guess = None

print("Welcome to Sia's Number Game!")
print("I am the result of 2 to the power of 5. Can you guess my number?")

while guess != secret_number:
    guess = int(input("Your guess: "))

    if guess < secret_number:
        print("Nope! Think bigger!")
    elif guess > secret_number:
        print("Nope! Think smaller!")
    else:
        print("Correct! 2^5 = 32. Sia approves! You are a math genius!")

