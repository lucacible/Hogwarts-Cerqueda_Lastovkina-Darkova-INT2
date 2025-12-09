#Chapter 2: The Journey to Hogwarts
from universe.characters import *

character = init_character()
def meet_friends(character):

    print("Hi ! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    choice = input("Your choice: ")

    if choice == "1":
        character["Attributes"]["loyalty"] = 1
    else:
        character["Attributes"]["ambition"] = 1

