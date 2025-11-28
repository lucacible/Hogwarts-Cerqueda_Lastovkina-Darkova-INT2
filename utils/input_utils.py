########################-Python to check user input and reading files, for utility functions-#################################

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
    number_str = input(message)
    try:
        number = int(number_str)

    except ValueError:
        print("Enter an integer : ")
        return ask_number(message,min_val,max_val)
    
    if min_val != None or max_val != None:
        if number >= max_val or number <= min_val:
            print("Enter a number between",min_val,"and",max_val)
            return ask_number(message,min_val,max_val)
        else:
            return number
    else:
        return number
        
#print(ask_number("Courage level : ", 1,10))



def ask_choice(message,options):
    
    
    
    
    






  