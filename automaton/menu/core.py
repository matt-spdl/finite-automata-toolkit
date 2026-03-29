from automaton import *
from .menu_class import *
from .utils import *

def menu_load_from_path():
    """Charge un automate depuis un chemin de fichier saisi par l'utilisateur."""
    display_header("Charger un automate par chemin")
    path = ask_path("Chemin vers le fichier de l'automate (Q pour annuler): ", allow_quit=True)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton


def menu_load_from_number():
    """Charge un automate depuis son numéro (1 à 44) dans le dossier automata_files."""
    display_header("Charger un automate par numéro")
    num = ask_int("Numéro de l'automate (Q pour annuler): ", 1, 44, allow_quit=True)
    path = get_path_to_automaton(num)
    automaton = read_automaton_from_file(path)
    print("Automate chargé avec succès !\n")
    return automaton


def menu_main():
    """Point d'entrée du menu principal : charge un automate puis ouvre le menu de l'automate."""
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
    """
    Menu interactif de reconnaissance de mot.
    Demande un mot à l'utilisateur et indique s'il est accepté ou rejeté par l'automate.

    Args:
        automaton : l'automate à utiliser pour la reconnaissance.
    """
    display_header("Reconnaissance de mot")
    while True:
        word = input("Mot à tester (Q pour annuler): ").strip()
        if word.lower() == "q":
            print("Test annulé.\n")
            return
        accepted = word_recognition(automaton, word)
        if accepted:
            print(f"Le mot '{word}' est accepté par l'automate.\n")
        else:
            print(f"Le mot '{word}' est rejeté par l'automate.\n")


def menu_automaton(automaton):
    """
    Menu de gestion d'un automate chargé : affichage, standardisation, AFDC, minimisation, etc.

    Args:
        automaton : l'automate à manipuler.
    """
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