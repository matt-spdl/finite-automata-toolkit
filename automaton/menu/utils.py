from pathlib import Path

class InputCancelled(Exception):
    """Exception levée si l'utilisateur annule l'entrée."""
    pass


def ask_path(prompt, allow_quit=False):
    """
    Demande à l'utilisateur de saisir un chemin de fichier.

    Args:
        prompt : le message affiché à l'utilisateur.
        allow_quit : si True, saisir "Q" lève InputCancelled.

    Returns:
        Un objet Path correspondant au chemin saisi.
    """
    while True:
        p = input(prompt).strip()
        if allow_quit and p.lower() == "q":
            raise InputCancelled()
        if p:
            return Path(p)
        print("Chemin vide.\n")


def ask_int(prompt, min_value=None, max_value=None, allow_quit=False):
    """
    Demande à l'utilisateur de saisir un entier, avec validation de plage.

    Args:
        prompt : le message affiché à l'utilisateur.
        min_value : valeur minimale acceptée (optionnel).
        max_value : valeur maximale acceptée (optionnel).
        allow_quit : si True, saisir "Q" lève InputCancelled.

    Returns:
        L'entier saisi par l'utilisateur.
    """
    while True:
        raw = input(prompt).strip()
        if allow_quit and raw.lower() == "q":
            raise InputCancelled()
        try:
            n = int(raw)
        except ValueError:
            print("Veuillez entrer un entier.\n")
            continue
        if min_value is not None and n < min_value:
            print(f"Valeur trop petite (min {min_value}).\n")
            continue
        if max_value is not None and n > max_value:
            print(f"Valeur trop grande (max {max_value}).\n")
            continue
        return n


def get_path_to_automaton(choice):
    """
    Retourne le chemin absolu vers le fichier d'automate correspondant au numéro donné.

    Args:
        choice : le numéro de l'automate.

    Returns:
        Un objet Path vers le fichier correspondant.
    """
    project_root = Path(__file__).resolve().parents[2]
    return (project_root / "automata_files" / f"a{choice}.txt").resolve()

def display_header(title):
    """
    Affiche un en-tête encadré dans la console.

    Args:
        title : le texte à afficher dans l'en-tête.
    """
    padding = 5
    padded_message = " " * padding + title + " " * padding
    length = len(padded_message)

    print("╔" + "═" * length + "╗")
    print("║" + padded_message + "║")
    print("╚" + "═" * length + "╝")