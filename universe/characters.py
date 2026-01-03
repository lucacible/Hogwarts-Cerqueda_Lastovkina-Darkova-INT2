
def init_character(last_name, first_name, attributes):
    character = {
        "First Name": first_name,
        "Last Name": last_name ,
    "Money": 100, 
    "Inventory": [],
    "Spells": [],
    "Attributes": attributes
    }
    return character

def display_character(character):
        print("First Name:",character["First Name"])
        print("Last Name:",character["Last Name"])
        print("Money:",character["Money"])
        inventory = ", ".join(character['Inventory'])
        print('Inventory: ', inventory)
        spells = ", ".join(character['Spells'])
        print('Spells: ', spells)
        print("Attributes: ", character['Attributes'])

def modify_money(character, amount):
    character['Money'] += amount

def add_item(character, key, item):
    character[key].append(item)