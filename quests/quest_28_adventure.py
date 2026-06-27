#!/usr/bin/env python3

def start():
    print("=== MURDER AT THE PARTY ===")
    print("Detective Sia, we need your help!")
    print("Doctor Johnson was found dead at the party.")
    print("There are 4 suspects: The Writer, The Wife, The Mistress, and The Mayor.")
    print("You must find the killer!")
    choice = input("\nWho do you want to interrogate first? (writer/wife/mistress/mayor): ").strip().lower()

    if choice == "writer":
        interrogate_writer()
    elif choice == "wife":
        interrogate_wife()
    elif choice == "mistress":
        interrogate_mistress()
    elif choice == "mayor":
        interrogate_mayor()
    else:
        print("That person is not a suspect. Game over!")

def interrogate_writer():
    print("\n📝 The Writer looks nervous...")
    print("Writer: I was just reading my book in the corner all night!")
    print("You notice ink stains on her hands... and something else.")
    print("You find a torn page from her notebook near the body.")
    clue = input("\nDo you CONFRONT her about the page or CHECK other suspects first? (confront/check): ").strip().lower()

    if clue == "confront":
        print("\nWriter: I... I can explain!")
        print("She starts sweating. She knows you know.")
        accuse()
    elif clue == "check":
        print("\nSmart move Detective Sia! Gather more evidence first.")
        second_suspect()
    else:
        print("You stood there confused. The killer escaped. Game over!")

def interrogate_wife():
    print("\n👩 The Wife is crying dramatically...")
    print("Wife: I loved my husband! Why would I kill him?")
    print("But you notice she is not actually crying. No tears.")
    print("She has a strong alibi though - 10 people saw her dancing all night.")
    print("\nShe seems innocent...")
    second_suspect()

def interrogate_mistress():
    print("\n💋 The Mistress seems calm. Too calm.")
    print("Mistress: The Doctor was going to leave his wife for me.")
    print("Why would I kill someone who loved me?")
    print("She has a point... and an alibi too.")
    print("\nShe seems innocent...")
    second_suspect()

def interrogate_mayor():
    print("\n🏛️ The Mayor is sweating nervously...")
    print("Mayor: I barely knew the Doctor! We met once at a conference!")
    print("You check his phone... only one message to the Doctor about a golf game.")
    print("\nThe Mayor seems innocent...")
    second_suspect()

def second_suspect():
    print("\nYou have gathered some clues. Time to make a decision!")
    accuse()

def accuse():
    print("\n🔍 Detective Sia, who is the killer?")
    suspect = input("Accuse: (writer/wife/mistress/mayor): ").strip().lower()

    if suspect == "writer":
        print("\n🎉 CORRECT!")
        print("The Writer confesses!")
        print("The Doctor had stolen her unpublished manuscript and published it as his own!")
        print("She poisoned his drink during the party.")
        print("Justice is served! Detective Sia solves the case! YOU WIN!")
    elif suspect == "wife":
        print("\n💀 WRONG!")
        print("The Wife was innocent. She was actually planning a surprise party for him.")
        print("The real killer escapes. Game over!")
    elif suspect == "mistress":
        print("\n💀 WRONG!")
        print("The Mistress was innocent. She loved the Doctor.")
        print("The real killer escapes. Game over!")
    elif suspect == "mayor":
        print("\n💀 WRONG!")
        print("The Mayor was innocent. He fainted when he heard the news.")
        print("The real killer escapes. Game over!")
    else:
        print("That is not a valid suspect. The killer escapes. Game over!")

start()
