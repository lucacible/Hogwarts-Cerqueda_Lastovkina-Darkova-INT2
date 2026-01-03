
from universe.characters import *
from utils.input_utils import ask_choice

houses = {
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
}



def update_house_points(houses,house_name,points):

    for key in houses.keys():
        if key == house_name:
           print("Changes to ",house_name,":",houses[house_name],"+", points)
           houses[house_name] = houses[house_name] + points
           print("New total points :",houses[house_name])
           return houses[house_name]
    else:
        return "This house does not exist"
   


def display_winning_house(houses):
    winning_house=[]
    
    for subkey,subvalue in houses.items():
        if subvalue>score:
            winning_house = [subkey]
            score=subvalue
        elif subvalue==score:
            winning_house.append(subkey)
    
    if len(winning_house)>1:
        print("The winning houses are :")
    else:
        print("The winning house is :")
    for house in winning_house:
        if winning_house.index(house)<len(winning_house)-1:
            print(house,end=", ")
        else:
            print(house,end=".")



def assign_house(character, questions):
 
    house_score={
        "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
    }

    info = character["Attributs"]
    house_score["Gryffindor"]= info["Gryffindor"]+value*2
    house_score["Slytherin"]=info["Slytherin"]+2*value
    house_score["Hufflepuff"]=info["Hufflepuff"]+2*value
    house_score["Ravenclaw"]=info["Ravenclaw"]+2*value

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

