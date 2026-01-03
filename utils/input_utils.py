
import json

def ask_text(message):
   
    text = input(message)
    while text == "" or text.isspace():
        print("No content")
        text=input(message)
    return text



def ask_number(message,min_val=None,max_val=None):


    nb_string=input(message)
    nb_string=nb_string.strip()

    negative=False
    if nb_string[0]=="-":
        negative=True
        nb_string=nb_string[1:]
    elif nb_string[0]=="+":
        nb_string=nb_string[1:]
        

    number=0
    for char in nb_string:
        if ord(char)<ord("0") or ord(char)>ord("9"):
            print("This is not a valid number")
            return ask_number(message,min_val,max_val)
    
    for dizaine in range(len(nb_string)):
        number = number * 10 + (ord(nb_string[dizaine])-ord("0"))

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
        
            

    


def ask_choice(message,options)->int:

    print(message)
    for i in range (len(options)):
        print(i+1,".",options[i])
    return ask_number("Your choice :",1,len(options))
    



    
def load_file(file_path):

    with open (file_path, "r",encoding='utf-8')as f:
        content=json.load(f)
        return content
    




  