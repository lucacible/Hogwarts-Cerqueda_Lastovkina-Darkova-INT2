#Chapter 1 of the game
from utils.input_utils import ask_choice, ask_number, ask_text
from universe.characters import init_character, dislay_character





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

    choice=ask_choice("So what will you do?",
    ["I will enter the HOGWARTS magic academy",
    "THIS IS BULLSHIT!!!, not going to your strange place."])
    
    
    intro_text3="""
GOOOOOOOOD, you see you're a smart boy. Welcome to this new life of yours.  
Now that's done, shouldn't you introduce yourself to this lovely letter???    
"""
    if choice==2:
        return("GAME OVER, DUH WHAT DID YOU EXPECT HUH?")
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

    character=init_character(first_name,last_name,Attributes)
    print(dislay_character(character))

introduction()
create_character()


    
