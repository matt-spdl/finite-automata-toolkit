from automaton import *
from automaton.menu.menu_class import *
from automaton.menu.utils import *

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
            return automaton
        accepted = word_recognition(automaton, word)
        if accepted:
            print(f"Le mot '{word}' est accepté par l'automate.\n")
        else:
            print(f"Le mot '{word}' est rejeté par l'automate.\n")


def _display_before_after(before_automaton, after_automaton, algorithm_label):
    print("Avant :")
    display_automaton_table(before_automaton)
    print("")
    print(f"Après {algorithm_label} :")
    display_automaton_table(after_automaton)
    print("")


def menu_display(automaton):
    """Affiche l'automate selon le choix de l'utilisateur."""
    menu = Menu("Affichage", {
        "1": MenuOption("Afficher le tableau", lambda: "table"),
        "2": MenuOption("Afficher l'automate (print)", lambda: "repr"),
    })
    choice = menu.run()
    if choice is None:
        return automaton
    display_header(f"Affichage ({automaton.name})")
    if choice == "table":
        display_automaton_table(automaton)
        print("")
    elif choice == "repr":
        print(automaton)
        print("")
    return automaton


def menu_standardization(automaton):
    """Standardise l'automate si nécessaire."""
    display_header(f"Standardisation ({automaton.name})")
    if is_standard(automaton):
        print("L'automate est déjà standardisé.\n")
        return automaton
    try:
        std = standardization(automaton)
        print("Automate standardisé.\n")
        _display_before_after(automaton, std, "standardisation")
        return std
    except Exception as e:
        print(f"Erreur : {e}\n")
        return automaton


def menu_determinization(automaton):
    """Déterminise l'automate si nécessaire."""
    display_header(f"Déterminisation ({automaton.name})")
    if is_determinist(automaton):
        print("L'automate est déjà déterministe.\n")
        return automaton
    try:
        det = determinize(automaton)
        print("Automate déterminisé.\n")
        _display_before_after(automaton, det, "AFDC")
        return det
    except Exception as e:
        print(f"Erreur : {e}\n")
        return automaton


def menu_minimization(automaton):
    """Minimise l'automate."""
    display_header(f"Minimisation ({automaton.name})")
    try:
        minimized = Minimization(automaton)
        print("Automate minimisé.\n")
        _display_before_after(automaton, minimized, "minimisation")
        return minimized
    except Exception as e:
        print(f"Erreur : {e}\n")
        return automaton


def menu_complementary(automaton):
    """Calcule l'automate complémentaire (déterminisation + complétion si besoin)."""
    display_header(f"Complémentaire ({automaton.name})")
    try:
        working = automaton
        if not is_determinist(working):
            print("Automate non déterministe : déterminisation en cours...")
            working = determinize(working)
        if not is_complete(working):
            print("Automate non complet : complétion en cours...")
            working = completion(working)
        comp = complementarization(working)
        print("Automate complémentaire généré.\n")
        _display_before_after(automaton, comp, "complémentaire")
        return comp
    except Exception as e:
        print(f"Erreur : {e}\n")
        return automaton


def menu_automaton(automaton):
    """Menu de gestion d'un automate chargé : affichage, standardisation, AFDC, minimisation, etc.

    Args:
        automaton : l'automate à manipuler.
    """
    current = automaton
    menu = Menu(f"Menu automate ({current.name})", {
        "1": MenuOption("Affichage", lambda: menu_display(current)),
        "2": MenuOption("Standardisation", lambda: menu_standardization(current)),
        "3": MenuOption("Déterminisation", lambda: menu_determinization(current)),
        "4": MenuOption("Minimisation", lambda: menu_minimization(current)),
        "5": MenuOption("Reconnaissance de mot", lambda: menu_word_recognition(current)),
        "6": MenuOption("Complémentaire", lambda: menu_complementary(current)),
    })

    while True:
        result = menu.run()
        if result is None:
            return None
        if isinstance(result, Automaton):
            current = result
            menu.title = f"Menu automate ({current.name})"