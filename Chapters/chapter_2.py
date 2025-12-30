#Chapter 2: The Journey to Hogwarts

from utils.input_utils import ask_choice, load_file
from universe.house import *
import json

def meet_friends(character):
#meeting with Ron
    text = """
    You board the Hogwarts Express. The train slowly departs northward...
A red-haired boy enters your compartment, looking friendly.
— Hi! I'm Ron Weasley. Mind if I sit with you?
How do you respond?
"""
    print(text)
    choice = ask_choice("Your choice: ", ["Sure, have a seat!", "Sorry, I prefer to travel alone."])
    if choice == 1:
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
"""
    print(text)
    choice = ask_choice("Your choice: ", ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."])
    if choice == 1 :
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
"""
    print(text)
    choice = ask_choice("Your choice: ", ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])
    if choice == 1:
        character["Attributes"]["Ambition"] += 1
        print("Draco smirks: —Good choice.")
    elif choice == 2:
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
    print()


def welcome_message():
    input("Professor Dumbledore: — Welcome back and welcome. Before we begin our banquet, I would like to say a few words. And here they are: Nitwit! Blubber! Oddment! Tweak! Thank you.")
    print()

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
            ["Defence Against the Dark Arts", "Potions", "Herbology", "Care of Magical Creatures"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]
    character["House"] = assign_house(character, questions)
    print()
    print("The Sorting Hat exclaims:", character["House"], "!!!")


def enter_common_room(character):
    house = character["House"]
    house_data = load_file('data/houses.json')
    info = house_data[house]
    print("You follow the prefects through the castle corridors...")
    print(info['emoji'], " ", info["description"])
    print(info["installation_message"])
    colors = ", ".join(info["colors"])
    print("Your house colors:", colors)

def start_chapter_2(character):
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    print('Your final character is :', character)
    text = """
    Congratulations!! Your journey at Hogwarts is officially started 😉 and it means even MORE adventures. 
But first, you have some classes to attend to ! Good luck and be attentive, you don't want to be kicked off out of Hogwarts the first year! """
    print(text)
    return character