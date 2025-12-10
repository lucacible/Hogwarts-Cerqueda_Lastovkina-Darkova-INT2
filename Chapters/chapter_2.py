#Chapter 2: The Journey to Hogwarts
from utils.input_utils import ask_choice
from universe.characters import *

character = init_character()
def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward...")
#meeting with Ron
    print("A red-haired boy enters your compartment, looking friendly.")
    print("— Hi ! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    choice = ask_choice("Your choice: ", ["1", "2"])
    if choice == "1":
        character["Attributes"]["Loyalty"] += 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        character["Attributes"]["Ambition"] += 1
        print("Ron seems a bit sad: — It's okay, I won't disturb you more.")

#meeting with Hermione
    print("A girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    choice = ask_choice("Your choice: ", ["1", "2"])
    if choice == "1" :
        character['Attributes']['Intelligence'] += 1
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else:
        character['Attributes']['Courage'] += 1
        print("Hermione seems confused: — I see... I hope you'll have enough adventures then.")

#meeting with Draco:
    print("Then a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    choice = ask_choice("Your choice: ", ["1", "2", "3"])
    if choice == "1":
        character["Attributes"]["Ambition"] += 1
        print("Draco smirks: —Good choice.")
    elif choice == "2":
        character["Attributes"]["Loyalty"] += 1
        print("Draco frowns, annoyed. — You'll regret that!")
    else:
        character['Attributes']['Courage'] += 1
        print("Draco turns red, angry: —Don't rely on my friendship ever, you fool!")

    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!")
    print("Your updated attributes: ", character["Attributes"])


def welcome_message():
    input("Professor Dumbledore: — Welcome back and welcome. Before we begin our banquet, I would like to say a few words. And here they are: Nitwit! Blubber! Oddment! Tweak! Thank you.")

def sorting_ceremony(character):
    print()

#test
meet_friends(character)
