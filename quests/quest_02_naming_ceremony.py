#!/usr/bin/env python3
print("--- THE STORYBOOK OF DESTINY ---")
status = input("Is everything normal to you? (yes/no): ").strip().lower()

characters = {
    "1": ("Apple White", "Daughter of Snow White, destined to follow her classic fairytale."),
    "2": ("Raven Queen", "Daughter of the Evil Queen, who wants to rewrite her own destiny."),
    "3": ("Madeline Hatter", "Daughter of the Mad Hatter, who can hear the Narrators and loves tea."),
    "4": ("Briar Beauty", "Daughter of Sleeping Beauty, who wants to live life to the fullest before her 100-year nap.")
}

print("\nChoose your destiny:")
for num, (name, story) in characters.items():
    print(f"[{num}] {name}: {story}")

choice = input("\nSelect a number: ").strip()
if choice in characters:
    print(f"Destiny claimed: You are {characters[choice][0]}!")
else:
    print("You remain a Rebel without a script.")
