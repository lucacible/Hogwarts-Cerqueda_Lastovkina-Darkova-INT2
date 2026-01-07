import random
from utils.input_utils import load_file
from universe.house import update_house_points, display_winning_house
from universe.characters import display_character


def create_teams(house, team_data, is_player=False, player=None):
    team = {
        'name': house,
        'score': 0,
        'goals_scored': 0,
        'goals_blocked': 0,
        'caught_snitch': False,
        'players': team_data
    }
    if is_player == True:
        new_team = []
        team["players"][0] = "{} {} (Seeker)".format(player["First Name"], player["Last Name"])
        for plr in team["players"]:
            new_team.append(plr)
        
        team['players'] = new_team
    return team
        
def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal = random.randint(1, 10)
    if chance_goal >= 6:
        if player_is_seeker == True:
            scorer = attacking_team["players"][0]
            print("{} scores a goal for {}! (+10 points)".format(scorer, attacking_team["name"]))
        else:
            random_player = attacking_team["players"][random.randint(1, 6)]
            print("{} scores a goal for {}! (+10 points)".format(random_player, attacking_team["name"]))
        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
    else:
        defending_team["goals_blocked"] += 1
        print("{} blocks the attack!".format(defending_team["name"]))

def golden_snitch_appears():
    chance_snitch = random.randint(1, 6)
    if chance_snitch == 6:
        return True
    else:
        return False

def catch_golden_snitch(e1, e2):
    winner = random.choice([e1,e2])
    winner["caught_snitch"] = True
    winner["score"] += 150
    return winner

def display_score(e1,e2):
    text = """
    Current Score:
    -> {}: {} points
    -> {}: {} points
    """.format(e1['name'], e1['score'], e2['name'], e2['score'])
    print(text)

def display_team(house, team):
    print("{} team:".format(house))
    for player in team['players']:
        print("- {}".format(player))

def quidditch_match(character, houses):
    teams_quidditch = load_file('data/teams_quidditch.json')
    player_house = character['House']
    opposing_house = random.choice(houses)
    while player_house == opposing_house:
        opposing_house = random.choice(houses)
    player_team = create_teams(player_house, teams_quidditch[player_house]['players'], is_player=True, player=character)
    opposing_team = create_teams(opposing_house, teams_quidditch[opposing_house]['players'])
    display_team(player_house, player_team)
    display_team(opposing_house, opposing_team)
    print("You are playing for {} as a Seeker.".format(player_team['name']))
    rounds = 0
    while rounds <= 20:
        rounds += 1
        print("\n---- Round {} ----".format(rounds))
        counter_player_team = 0
        counter_opposing_team = 0
        if counter_player_team < counter_opposing_team or counter_player_team == counter_opposing_team:
            attempt_goal(player_team, opposing_team, player_is_seeker=True)
            display_score(player_team, opposing_team)
        else:
            attempt_goal(opposing_team, player_team, player_is_seeker=False)
            display_score(opposing_team, player_team)
        golden_snitch = golden_snitch_appears()
        if golden_snitch == True:
            print("The Golden Snitch has appeared!")
            catching_team = catch_golden_snitch(player_team, opposing_team)
            print("{} catches the Golden Snitch! (+150 points)".format(catching_team['name']))
            display_score(player_team, opposing_team)
            print("The match is over! {} wins!".format(catching_team['name']))
            break
        input("Press Enter to continue to the next round...")
    if rounds == 20:
        print("The match has ended after 20 rounds!")
        if player_team['score'] > opposing_team['score']:
            print("{} wins and earns 500 points!".format(player_team['name']))
            player_team['score'] += 500
        elif opposing_team['score'] > player_team['score']:
            print("{} wins and earns 500 points!".format(opposing_team['name']))
            opposing_team['score'] += 500
        else:
            print("It's a tie!")

    update_house_points(houses,player_team['name'],player_team['score'])
    update_house_points(houses,opposing_team['name'],opposing_team['score'])
    print("Final Results:")
    display_score(player_team, opposing_team)


def start_chapter_4_quidditch(character, houses):
    text = """
    The Quidditch season is about to begin at Hogwarts!

As a new student, you will be guided through your first match.
Get ready to take off, YOU WERE CHOSEN AS A SEEKER!
    """
    input(text)
    quidditch_match(character, houses)
    text2 = """
    The Quidditch season is coming to an end.
The game you showed was impressive! We are proud to have you in our team.
⭐ Congratulations on completing Chapter 4: The Quidditch Match! ⭐

Soooo, after all that time... we are about to announce the winner of the House Cap!
    """
    print(text2)
    print("And the winning house is...")
    display_winning_house(houses)
    print("Also, here is your final information:")
    display_character(character)
