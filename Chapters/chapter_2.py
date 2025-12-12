#Chapter 2: The Journey to Hogwarts

from utils.input_utils import ask_choice, load_file
from universe.house import *

def meet_friends(character):
#meeting with Ron
    text = """
    You board the Hogwarts Express. The train slowly departs northward...
A red-haired boy enters your compartment, looking friendly.
— Hi! I'm Ron Weasley. Mind if I sit with you?
How do you respond?
1. Sure, have a seat!
2. Sorry, I prefer to travel alone.
"""
    print(text)
    choice = ask_choice("Your choice: ", ["1", "2"])
    if choice == "1":
        character["Attributes"]["Loyalty"] += 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        character["Attributes"]["Ambition"] += 1
        print("Ron seems a bit sad: — It's okay, I won't disturb you more.")

#meeting with Hermione
    text = """
    A girl enters next, already carrying a stack of books.
— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?
How do you respond?
1. Yes, I love learning new things!
2. Uh… no, I prefer adventures over books.
"""
    print(text)
    choice = ask_choice("Your choice: ", ["1", "2"])
    if choice == "1" :
        character['Attributes']['Intelligence'] += 1
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else:
        character['Attributes']['Courage'] += 1
        print("Hermione seems confused: — I see... I hope you'll have enough adventures then.")

#meeting with Draco:
    text = """
    Then a blonde boy enters, looking arrogant.
— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?
How do you respond?
1. Shake his hand politely.
2. Ignore him completely.
3. Respond with arrogance.
"""
    print(text)
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
    text = """
    The train continues its journey. Hogwarts Castle appears on the horizon...
Your choices already say a lot about your personality!
"""
    print(text)
    print("Your updated attributes: ", character["Attributes"])


def welcome_message():
    input("Professor Dumbledore: — Welcome back and welcome. Before we begin our banquet, I would like to say a few words. And here they are: Nitwit! Blubber! Oddment! Tweak! Thank you.")

def sorting_ceremony(character):
    text = """
    The sorting ceremony begins in the Great Hall...
The Sorting Hat observes you for a long time before asking its questions:
"""
    print(text)
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "What is your favorite dish? Choose:",
            ["Butterbeer", "Blood Pops", "Chocolate Frogs", "Fizzing Whizzbees"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "In what course are you the most interested?",
            ["Transfiguration", "Potions", "Care of Magical Creatures", "Herbology"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]
    assign_house(character, questions)

import json
def enter_common_room(character):
    house_data = load_file('data/houses.json')
    print("You follow the prefects through the castle corridors...")
    print(house_data['emoji'], " ", house_data["description"])
    print(house_data["installation_message"])
    colors = ", ".join(house_data["colors"])
    print("Your house colors:", colors)

