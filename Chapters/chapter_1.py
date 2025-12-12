#Chapter 1 of the game
from utils.input_utils import ask_choice, ask_number, ask_text,load_file
from universe.characters import init_character, display_character,modify_money,add_item






def introduction():
    intro_text="""
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
#This part here gives the first text
    print(intro_text)
    input("TYPE ANYTHING TO CONTINUE")

    intro_text2="""
You brute force your way to the letter in it...or so you thought!!
Suddenly the envelope disappears from your hands and starts floating in the air.

A MOUTH?? opens:

"Dear student, we're happy to annouce that you've been accepted to the 
most prestigious HOGWARTS magic academy."

"Not befitting of you...moggle" whispers the letter??

"The ministry of magic affairs has chosen you to enter the magical 
circle, befitting your magical attributes.

"OHHHH...so you are not a totally incapable after all...hehe" Laughs the letter??

"You still have a choice though...though I'd recommend not skipping this opportunity"
"""
#This part the second text
    print(intro_text2)
    input("TYPE ANYTHING TO CONTINUE")

    choice = ask_choice("So what will you do?",
    ["I will enter the HOGWARTS magic academy",
    "THIS IS BULLSHIT!!!, I'm staying with Uncle."])
    
    
    intro_text3="""
GOOOOOOOOD, you see you're a smart boy. Welcome to this new life of yours.  
Now that's done, shouldn't you introduce yourself to this lovely letter???    
"""
    if choice== 2 :
        print("GAME OVER, DUH WHAT DID YOU EXPECT HUH?")
        exit()
    else:
        print(intro_text3)

        

#Down here is the function making you create your own character

def create_character():
    last_name=ask_text("Enter your character's last name: ")
    first_name=ask_text("Enter the character's first name: ")
    print()
    print("Choose your attributes:")
    
    Attributes={
        "Courage":0,
        "Intelligence":0,
        "Loyalty":0,
        "Ambition":0
    }
    Attributes["Courage"]=ask_number("Courage level (1-10): ")
    Attributes["Intelligence"]=ask_number("Intelligence level (1-10): ")
    Attributes["Loyalty"]=ask_number("Loyalty level (1-10): ")
    Attributes["Ambition"]=ask_number("Ambition level (1-10): ")

    character=init_character(last_name, first_name,Attributes)
    print()
    display_character(character)
    return character

#introduction()
#create_character()

def meet_hagrid(character):
    hagrid_text="""
Hagrid: Ohhhh, look how big he is haHaHah...
        I'll help you make your shopping in Diagon Alley.
"""
    choice=ask_choice("Do you want to follow Hagrid?",["Yes","No"])
    if choice==1:
        print("All right let's go!")
        exit()
    else:
        print("NO? Welp, you don't really have a choice...you leave for Diagon Alley.")


def buy_supplies(character):
    data_diagon= load_file("data/inventory.json")
    print("Datalog of available items:")
    required_items=[]
    for item_nb, cara in data_diagon.items():
        print(f"{item_nb}. {cara[0]} - {cara[1]} Galleons ({cara[2]})")
        if "required"==cara[2]:
            required_items.append(item_nb)
    
#faut que tu termines et que tu geres le systeme de sauvegarde vu avec mathieu (cf chapter_2.py)
#retablie toi bien 😊 !
    
    
    
    while character["Money"]>0 and required_items!=[]:
        
        print(f"You have {character["Money"]} Galleons")
        for item in required_items:
            print("Remaining required items: ",item, end=",")
        
        item_choice=ask_number("Enter the number of the item to buy")
        if data_diagon[item_choice][1]>character["Money"] and data_diagon[item_choice][2]=="required":
            print("You don't know how to count do you... Luckily you're going to Hogwarts")
            print("Game Over")
            exit()
        
        if data_diagon[item_choice][2]=="required":
            i=required_items.index[item_choice]
            required_items.remove[i]
        print(f"You bought : {data_diagon[item_choice][0]} (-{data_diagon[item_choice][1]} Galleons) .")
        modify_money(character,data_diagon[item_choice][1])
        add_item(character,"Inventory",data_diagon[item_choice])
    
    print("All required items have been purchased!")
    print()
    print("It's time to choose your Hogwarts pet!")
    print()
    print(f"You have {character["Money"]} Galleons")
    print()
    print("Available pets:")
    
    pets=["Owl","Cat","Rat","Toad"]
    price_pet=[20,15,10,5]
    for pet_indx in range(len(pets)-1):
        print(f"{pet_indx+1}. {pets[pet_indx]} - {price_pet[pet_indx]} Galleons")
    
    pet_choice=ask_choice("Which pet do you want?",pets)
    if price_pet[pet_choice]>character["Money"]:
        print("You don't know how to count do you... Luckily you're going to Hogwarts")
        print("Game Over")
        exit()
    
    modify_money(character,price_pet[pet_indx])
    add_item(character,"Inventory",pets[pet_choice])    
    print(f"You chose: {pets[pet_choice]} (-{price_pet[pet_choice]})")

    print("All required items have been successfully purchased!")
    print("Here is your final inventory:")
    print()
    display_character(character)
    return character  

def start_chapter_1():
    introduction()
    create_character()
    meet_hagrid(create_character)
    buy_supplies(create_character)
    end_chapter_1_text="""
Contrats, this is the end of Chapter 1, your adventure in Hogwarts is only
starting, so don't too cocky jeje.
"""
    print(end_chapter_1_text)
    print("Your final character is:")
    display_character(character)
        





