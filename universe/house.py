#Python for choice and management of the house  
from universe.characters import *
from utils.input_utils import ask_choice

houses = {
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
}



def update_house_points(houses,house_name,points):
    """
This function takes as input the scores of the houses and updates them
according to a number given.Then displays the new score and uptdates the
the dictionary containing all house scores.
"""
    #all of this is for displaying in a readable way
    for key in houses.keys():
        if key == house_name:
           print("Changes to ",house_name,":",houses[house_name],"+", points)
           houses[house_name] = houses[house_name] + points
           print("New total points :",houses[house_name])
           return houses[house_name]
    else:
        return "This house does not exist"
    
#print(update_house_points(houses,"Gryffindor",-6))


def display_winning_house(dico):
    """
This function takes the houses dictionary and displays the winning houses
relative to their current scores
Input: houses
Output:List winning_house
"""   
    
    score=dico["Gryffindor"]
    winning_house=[]
    #we look for the highest scores and add them in the list
    for subkey,subvalue in dico.items():
        if subvalue>score:
            winning_house = [subkey]
            score=subvalue
        elif subvalue==score:
            winning_house.append(subkey)
    #we look if there is one or more winning houses
    if len(winning_house)>1:
        print("The winning houses are :")
    else:
        print("The winning house is :")
    for house in winning_house:
        if winning_house.index(house)<len(winning_house)-1:
            print(house,end=", ")
        else:
            print(house,end=".")

#print(displya_winning_house(houses))

def assign_house(character, questions):
    """
This function takes as input your character dictionary and questions needed to determine your house and displays the house
more attuned with
Input: characters and tuples questions
Output: the house your're more attuned with
"""
    house_score={
        "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
    }
    
    for attri,value in character["Attributes"].items():
        match attri:
            case "Courage":
                house_score["Gryffindor"]=  house_score["Gryffindor"]+value*2
            case "Ambition":
                house_score["Slytherin"]=house_score["Slytherin"]+2*value
            case "Loyalty":
                house_score["Hufflepuff"]=house_score["Hufflepuff"]+2*value
            case "Intelligence":
                house_score["Ravenclaw"]=house_score["Ravenclaw"]+2*value
    
    
    for q in range(len(questions)):
        choice_nb=ask_choice(questions[q][0],questions[q][1])
        choice=questions[q][2][choice_nb-1]
        update_house_points(house_score,choice,3)
    return display_winning_house(house_score)

"""
character=init_character("Luca","Cerqueda",{"Courage":5,"Ambition":8,"Loyalty":6,"Intellinge":10})
assign_house(character, [ 
( 
"You see a friend in danger. What do you do?", 
["Rush to help", "Think of a plan", "Seek help", "Stay calm and obserbe"],
 
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
), 
( 
"Which trait describes you best?", 
["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"], 
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
), 
( 
"When faced with a difficult challenge, you...", 
["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", 
"Analyze the problem"], 
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
) 
])
"""