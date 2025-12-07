#Python for choice and management of the house  
houses = {
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
}



def update_house_points(dico,house_name,points):
    """
This function takes as input the scores of the houses and updates them
according to a number given.Then displays the new score and uptdates the
the dictionary containing all house scores.
"""
    for key in dico.keys():
        if key == house_name:
           print("Changes to ",house_name,":",dico[house_name],"+", points)
           dico[house_name] = dico[house_name] + points
           print("New total points :")
           return dico[house_name]
    else:
        return "This house does not exist"
    
#print(update_house_points(houses,"Gryffindor",-6))


def displya_winning_house(dico):
    