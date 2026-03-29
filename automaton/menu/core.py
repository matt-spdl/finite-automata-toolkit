from automaton import *
from menu_class import *
from input_utils import *

def load_from_path():
    path = ask_path("Chemin vers le fichier de l'automate (Q pour annuler): ", allow_quit=True)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton

def load_from_number():
    num = ask_int("Numéro de l'automate (Q pour annuler): ", 1, 44, allow_quit=True)
    path = get_path_to_automaton(num)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton

def menu_automaton(automaton):
    menu = Menu("Menu automate", {
        "1": MenuOption("Affichage", lambda: None),
        "2": MenuOption("Standardisation", lambda: None),
        "3": MenuOption("AFDC", lambda: None),
        "4": MenuOption("Minimisation", lambda: None),
        "5": MenuOption("Reconnaissance", lambda: None),
        "6": MenuOption("Complémentaire", lambda: None),
        "7": MenuOption("Recharger / Quitter", lambda: None),
    })
    return menu.run()

def menu_main():
    menu = Menu("Menu principal", {
        "1": MenuOption("Charger automate par chemin", load_from_path),
        "2": MenuOption("Charger automate par numéro", load_from_number),
    })
    while True:
        automaton = menu.run()
        if automaton is None:
            print("Au revoir !")
            return
        menu_automaton(automaton)

if __name__ == "__main__":
    menu_main()