import random
from universe.characters import add_item
from universe.house import update_house_points,display_winning_house
from universe.characters import display_character
from utils.input_utils import load_file

def learn_spells(character, file_path="data/spells.json"):
    
    data_spells= load_file(file_path)
    offensive_spells=[]
    defensive_spells=[]
    utility_spells=[]
    
    
    for spell in data_spells:
        match spell["type"]:
            case "Offensive":
                offensive_spells.append(spell["name"])
            case "Defensive":
                defensive_spells.append(spell["name"])
            case "Utility":
                utility_spells.append(spell["name"])
    
    offensive=random.choice(offensive_spells)
    print(f"You have just learned the spell:{offensive} (Offensive)")
    add_item(character,character["Spells"],offensive)
    input("Press Enter to continue...")
    print()

    defensive=random.choice(defensive_spells)
    print(f"You have just learned the spell:{defensive} (Defensive)")
    add_item(character,character["Spells"],defensive)
    input("Press Enter to continue...")
    print()

    for i in range(3):
        utility=random.choice(utility_spells)
        print(f"You have just learned the spell:{utility} (Utility)")
        print()
        utility_spells.remove(utility)
        add_item(character,character["Spells"],utility)
        input("Press Enter to continue...")
        print()

    
    text="""
You have completed your basic spell training at Hogwarts! 
Here are the spells you now master: 
"""
    print(text)
    for spell_char in character["Spells"]:
        for spell_nb in data_spells:
            if spell_char==spell_nb["name"]:
                print(f"- {spell_nb["name"]} {spell_nb["type"]} : {spell_nb["description"]}")
    

def magic_quiz(character,file_path="data/magic_quiz.json"):
    
    data_questions=load_file(file_path)
    
    print("Welcome to your favourite Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    
    score=0
    for nb in range(4):
        question=random.choice(data_questions)
        data_questions.remove(question)
        
        print(f"{question["question"]}")
        ans=input(">")
        
        if ans==question["answer"]:
            print(f"Correct answer! +25 points for your house.")
            score+=25
        else:
            print(f"Wrong answer. The correct answer was: {question["answer"]}")
    
    print(f"Score obtained {score}")
    return score
    

def start_chapter_3(character, houses):
    
    learn_spells(character)
    score=magic_quiz(character)
    update_house_points(houses,character["House"],score)
    display_winning_house(houses)
    display_character(character)
    return character, houses