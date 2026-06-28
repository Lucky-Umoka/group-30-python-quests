#!/usr/bin/env python3

# Quest 30: The Reflective Scribe
# Sia Virginie - Level 6
# Revisiting 3 quests with detailed comments

# ─────────────────────────────────────────
# QUEST 25 REVISITED - Number Wizard
# ─────────────────────────────────────────

# We store the secret number in a variable
# This makes it easy to change later
secret_number = 32
guess = None  # None means empty, no answer yet

print("Welcome to Sia's Number Game!")
# We use a while loop because we don't know
# how many attempts the user will need
while guess != secret_number:
    # int() converts the text input to a number
    # so we can compare it mathematically
    guess = int(input("Your guess: "))

    if guess < secret_number:
        print("Nope! Think bigger!")
    elif guess > secret_number:
        print("Nope! Think smaller!")
    else:
        # This only runs when guess == secret_number
        # which also stops the while loop
        print("Correct! 2^5 = 32. Sia approves! You are a math genius!")


# ─────────────────────────────────────────
# QUEST 29 REVISITED - Bank Heist
# ─────────────────────────────────────────

SECRET_CODE = 32    # Stored as a constant - easy to change
MAX_ATTEMPTS = 3    # Maximum tries before game over

print("\n=== THE BANK HEIST ===")
print("Hint: (6 x 5) + (5 - 3) + (2 x 3) - 6 = ???")

# range(1, MAX_ATTEMPTS + 1) counts 1, 2, 3
# This is more human-friendly than 0, 1, 2
for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"\nAttempt {attempt}/3 - Enter the code: "))

    if guess == SECRET_CODE:
        print("WAOUH! The true successor of the Prison Break actor!")
        print("He is really your role model! YOU WIN!")
        break    # break stops the loop immediately when correct
    else:
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print("Did you even watch Prison Break?!")
            print(f"{remaining} attempt(s) left!")
        else:
            # This runs after the last wrong attempt
            print("You clearly never watched Prison Break. Game over!")


# ─────────────────────────────────────────
# QUEST 27 REVISITED - Social Media FizzBuzz
# ─────────────────────────────────────────

print("\n=== Sia's Social Media FizzBuzz ===")

# range(1, 101) generates numbers from 1 to 100
# 101 is excluded so we stop at 100
for number in range(1, 101):

    # We MUST check the combined condition first!
    # If we checked % 3 first, 15 would print
    # Snapchat instead of YouTube
    if number % 3 == 0 and number % 5 == 0:
        print("YouTube")    # Divisible by both 3 and 5
    elif number % 3 == 0:
        print("Snapchat")   # Divisible by 3 only
    elif number % 5 == 0:
        print("TikTok")     # Divisible by 5 only
    else:
        print(number)       # Not divisible by either

