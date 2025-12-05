########################-Python to check user input and reading files, for utility functions-#################################
import json

def ask_text(message):
    """
    Funtion that checks if the input given by the user is correct

        Checks if it is not empty or whitespace
    Input: The user enters a string


    Ouptut: returns the text entered by the user if it is correct,
            else it asks it again
    
    """
    text = input(message)
    while text == "" or text.isspace():
        print("No content")
        text=input(message)
    return text



def ask_number(message,min_val=None,max_val=None):
    """
This function takes a number entered by the user and verifies 
its validity
Input: the user enters a number
Ouptut: Displays the number entered by the user


"""
    nb_string=input(message)
    nb_string=nb_string.strip()
#We verify if the number is negative or not
    negative=False
    if nb_string[0]=="-":
        negative=True
        nb_string=nb_string[1:]
    elif nb_string[0]=="+":
        nb_string=nb_string[1:]
        
#We transform the number from a string into a integer      
    number=0
    for dizaine in range(len(nb_string)):
        number = number * 10 + (ord(nb_string[dizaine])-ord("0"))
#We verify wether the number is in the boundaries set or not
    if negative==True:
        number= (-number)
    if max_val!=None or min_val!=None:
        if number>max_val:
            print("The input number is to high")
            return ask_number(message,min_val,max_val)
        elif number<min_val:
            print("The input number is to low")
            return ask_number(message,min_val,max_val)
        else:
            return  number
    else:      
        return number
        
            

    
#print(ask_number("Courage level : ", 1,10))



def ask_choice(message,options):
    """
This function displays a number of options to the user and then asks for the user's choice, which it returns
Input; the user enters the number of his choice
Output: returns the user's choice so that it can later used in the main code
"""
    print(message)
    for i in range (len(options)):
        print(i+1,".",options[i])
    return ask_number("Your choice :")
    

#print(ask_choice("Do you want to continue?",["Yes", "No"]))

    
def load_file(file_path):
    with open (file_path, "r",encoding='utf-8')as f:
        content=json.load(f)
        return content
    
#print(load_file("data/houses.json"))






  