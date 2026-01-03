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

    info = character["Attributs"]
    house_score["Gryffindor"]=  house_score["Gryffindor"]+value*2
    house_score["Slytherin"]=house_score["Slytherin"]+2*value
    house_score["Hufflepuff"]=house_score["Hufflepuff"]+2*value
    house_score["Ravenclaw"]=house_score["Ravenclaw"]+2*value

    i = 0
    for question, options, house in questions:
        choice_nb = ask_choice(question, options)
        while i < len(options):
            if options[i] == choice_nb:
                final_house = house[i]
                house_score[final_house] += 3
            i += 1
        print('Final house scores:', house_score)
        highest_score = None
        winning_house = None
        if highest_score == None or house_score[final_house] > highest_score:
            highest_score = house_score[final_house]
            winning_house = final_house
        return winning_house

