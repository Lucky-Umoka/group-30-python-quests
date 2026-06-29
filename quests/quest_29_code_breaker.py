#!/usr/bin/env python3

SECRET_CODE = 32
MAX_ATTEMPTS = 3

print("=== THE BANK HEIST ===")
print("You are inside the bank. The vault is right in front of you!")
print("Security arrives in 3 minutes. You have 3 attempts to crack the code!")
print("\nHint: (6 x 5) + (5 - 3) + (2 x 3) - 6 = ???")

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"\nAttempt {attempt}/3 - Enter the code: "))

    if guess == SECRET_CODE:
        print("\nCLICK! The vault opens!")
        print("You grab the money and run!")
        print("WAOUH! The true successor of the Prison Break actor!")
        print("He is really your role model! YOU WIN! Mission accomplished!")
        break
    else:
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print("You did not pay attention in math class!")
            print(f"Did you even watch Prison Break?! {remaining} attempt(s) left!")
        else:
            print("ALARM! ALARM! The police are here!")
            print("You clearly never watched Prison Break. Game over!")

