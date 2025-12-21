#Python for the main menu of the game
from utils.input_utils import ask_choice
from universe.house import houses
from Chapters.chapter_1 import start_chapter_1
from Chapters.chapter_2 import start_chapter_2
from Chapters.chapter_3 import start_chapter_3

def display_main_menu():
    main_game_menu = """
    1. Start Chapter 1 - Arrival in the magical world.
    2. Exit the game.
    """
    return main_game_menu

def launch_menu_choice():
    choice = ask_choice(display_main_menu(), ["Start", "Exit"])
    if choice == 1:
        character = start_chapter_1()
        start_chapter_2(character)
        start_chapter_3(character, houses)
        #start_chapter_4_quidditch(character, houses)
    elif choice == 2:
        print("Thank you for your attention! Hogwarts hopes to see you among its students in the future!")
        exit()
    else:
        print("Please enter a valid option.")
        launch_menu_choice()
