#Python for character creation and management
#Python for characters
def init_character(last_name, first_name, attributes):
    character = {
    "Personal information": {
        "First Name": first_name,
        "Last Name": last_name },
    "Money": 100, #in galleons
    "Inventory": ['a','b'],
    "Spells": [],
    "Attributes": attributes
    }
    return character

def dislay_character(character):
    for key in character.keys():
        value = character[key]
        for subkey,subvalue in value.items():
            print("{}: {}".format(subkey,subvalue))
        for element in value:
            text = ", ".join(value)
            print(text)
        print(value)


#test
atts = {"power": 150, "speed": 100}
player = init_character("Darkova", "Dina", atts)
dislay_character(player)