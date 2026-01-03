from utils.input_utils import ask_choice, ask_number, ask_text, load_file
from universe.characters import init_character, display_character, modify_money, add_item
import json


def introduction():
    intro_text = """
For as long as you can remember strange things have been happening around you.
Ghosts seem to linger in your house, voices keep whispering their sweet words,
windows move on their own.

Today your house feels especially cold, as if something that will change your life is
coming, you can feel it, the longing, that sweet ecstasy coursing through your body.

ITS COMING!!! ITS HERE??
"tap...tap...tap"
"What is that?"

A strange envelope has appeared in front of your room's window. Pristine white in color
marked with a clear red signet.

"HOGWARTS Magic academy???"
"Is it what I've been waiting for?"

"""
    # This part here gives the first text
    print(intro_text)
    input()

    intro_text2 = """
You brute force your way to the letter in it...or so you thought!!
Suddenly the envelope disappears from your hands and starts floating in the air.

A MOUTH?? opens:

"Dear student, we're happy to announce that you've been accepted to the
most prestigious HOGWARTS magic academy."

"Not befitting of you...moggle" whispers the letter??

"The ministry of magic affairs has chosen you to enter the magical
circle, befitting your magical attributes.

"OHHHH...so you are not a totally incapable after all...hehe" Laughs the letter??

"You still have a choice though...though I'd recommend not skipping this opportunity"
"""
    # This part the second text
    print(intro_text2)
    input()

    choice = ask_choice("So what will you do?",
                        ["I will enter the HOGWARTS magic academy",
                         "THIS IS BULLSHIT!!!, I'm staying with Uncle."])

    intro_text3 = """
GOOOOOOOOD, you see you're a smart boy. Welcome to this new life of yours.  
Now that's done, shouldn't you introduce yourself to this lovely letter???    
"""
    if choice == 2:
        print("GAME OVER, DUH WHAT DID YOU EXPECT HUH?")
        exit()
    else:
        print(intro_text3)

def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter the character's first name: ")
    print()
    print("Choose your attributes:")

    Attributes = {
        "Courage": 0,
        "Intelligence": 0,
        "Loyalty": 0,
        "Ambition": 0
    }
    Attributes["Courage"] = ask_number("Courage level (1-10): ")
    Attributes["Intelligence"] = ask_number("Intelligence level (1-10): ")
    Attributes["Loyalty"] = ask_number("Loyalty level (1-10): ")
    Attributes["Ambition"] = ask_number("Ambition level (1-10): ")

    character = init_character(last_name, first_name, Attributes)
    print()
    print("This is your character information for the moment: ")
    display_character(character)
    print()
    return character


def meet_hagrid(character):
    hagrid_text = """
Hagrid: Ohhhh, look how big he is haHaHah...
        I'll help you make your shopping in Diagon Alley.
"""
    print(hagrid_text)
    choice = ask_choice("Do you want to follow Hagrid?", ["Yes", "No"])
    if choice == 1:
        print()
        print("All right let's go!")
    else:
        print()
        print("NO? Welp, you don't really have a choice...you leave for Diagon Alley.")
        exit()


def buy_supplies(character):
    data_diagon = load_file("data/inventory.json")
    print("Catalog of available items:")
    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]
    for item_nb, value in data_diagon.items():
        label = "required" if value[0] in required_items else ""
        print("{}. {} - {} Galleons {}".format(item_nb, value[0], value[1], label))

    while character["Money"] > 0 and required_items != []:
        print()
        print(f"You have {character['Money']} Galleons")
        print("Remaining required items:", end=" ")
        for item in required_items:
            if required_items.index(item) < len(required_items) - 1:
                print(item, end=", ")
            else:
                print(item)

        item_choice = ask_text("Enter the number of the item to buy :")
        if data_diagon[item_choice][1] > character["Money"] and data_diagon[item_choice][0] in required_items:
            print("You don't know how to count do you... Luckily you're going to Hogwarts")
            print("Game Over")
        elif data_diagon[item_choice][0] in required_items:
            required_items.remove(data_diagon[item_choice][0])

        print(f"You bought : {data_diagon[item_choice][0]} (-{data_diagon[item_choice][1]} Galleons) .")
        modify_money(character, -data_diagon[item_choice][1])
        add_item(character, "Inventory", data_diagon[item_choice][0])

    print("All required items have been purchased!")
    print()
    print("It's time to choose your Hogwarts pet!")
    print()
    print(f"You have {character['Money']} Galleons")
    print()
    print("Available pets:")

    pets = ["Owl", "Cat", "Rat", "Toad"]
    price_pet = [20, 15, 10, 5]
    for pet_indx in range(len(pets)) :
        print(f"{pet_indx + 1}. {pets[pet_indx]} - {price_pet[pet_indx]} Galleons")

    pet_choice = ask_choice("Which pet do you want?", pets)
    if price_pet[pet_choice] > character["Money"]:
        print("You don't know how to count do you... Luckily you're going to Hogwarts")
        print("Game Over")
        exit()

    modify_money(character, price_pet[pet_indx])
    add_item(character, "Inventory", pets[pet_choice])
    print(f"You chose: {pets[pet_choice]} (-{price_pet[pet_choice]})")

    print("All required items have been successfully purchased!")
    print("Here is your final inventory:")
    print("")
    inventory = ", ".join(character["Inventory"])
    print(inventory)
    print("Your Character Profile:")
    display_character(character)
    return character


def start_chapter_1():
    introduction()
    character = create_character()
    meet_hagrid(character)
    buy_supplies(character)
    end_chapter_1_text = """
Contrats, this is the end of Chapter 1, your adventure in Hogwarts is only
starting, so don't too cocky jeje.
"""
    print(end_chapter_1_text)
    print("Your final character is:")
    display_character(character)
    return character
