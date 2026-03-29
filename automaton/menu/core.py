from automaton import *
from menu_class import *
from utils import *

def menu_load_from_path():
    display_header("Charger un automate par chemin")
    path = ask_path("Chemin vers le fichier de l'automate (Q pour annuler): ", allow_quit=True)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton


def menu_load_from_number():
    display_header("Charger un automate par numéro")
    num = ask_int("Numéro de l'automate (Q pour annuler): ", 1, 44, allow_quit=True)
    path = get_path_to_automaton(num)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton


def menu_main():
    menu = Menu("Menu principal", {
        "1": MenuOption("Charger automate par chemin", menu_load_from_path),
        "2": MenuOption("Charger automate par numéro", menu_load_from_number),
    })
    while True:
        automaton = menu.run()
        if automaton is None:
            print("Au revoir !")
            return
        menu_automaton(automaton)


def menu_word_recognition(automaton):
    display_header("Reconnaissance de mot")
    while True:
        word = input("Mot à tester (Q pour annuler): ").strip()
        if word.lower() == "q":
            print("Test annulé.\n")
            return
        accepted = automaton.word_recognition(automaton, word)
        if accepted:
            print(f"Le mot '{word}' est accepté par l'automate.\n")
        else:
            print(f"Le mot '{word}' est rejeté par l'automate.\n")


def menu_automaton(automaton):
    menu = Menu(f"Menu automate ({automaton.name})", {
        "1": MenuOption("Affichage", lambda: None),
        "2": MenuOption("Standardisation", lambda: None),
        "3": MenuOption("AFDC", lambda: None),
        "4": MenuOption("Minimisation", lambda: None),
        "5": MenuOption("Reconnaissance de mot", menu_word_recognition),
        "6": MenuOption("Complémentaire", lambda: None),
    })
    return menu.run()

if __name__ == "__main__":
    menu_main()