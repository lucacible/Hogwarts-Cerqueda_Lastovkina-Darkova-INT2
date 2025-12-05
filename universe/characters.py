#Python for character creation and management
#Python for characters
def init_character(last_name, first_name, attributes):
    character = {
    "First Name": first_name,
    "Last Name": last_name,
    "Money": 100, #in galleons
    "Inventory": ['a','b'],
    "Spells": [],
    "Attributes": attributes
    }
    return character

def dislay_character(character):
    for key,value in character.items():
        if key == "Inventory" and key == 'Spells':
            text = ', '.join(key)
            print(text)
        print('{}: {}'.format(key,value))


#test
atts = {"power": 150, "speed": 100}
player = init_character("Darkova", "Dina", atts)
dislay_character(player)

from utils.input_utils import ask_number
def modify_money(character, amount):
    amount = ask_number('Which amount of money?')
