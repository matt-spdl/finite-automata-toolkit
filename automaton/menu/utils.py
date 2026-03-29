from pathlib import Path

class InputCancelled(Exception):
    """Exception levée si l'utilisateur annule l'entrée."""
    pass


def ask_path(prompt, allow_quit=False):
    while True:
        p = input(prompt).strip()
        if allow_quit and p.lower() == "q":
            raise InputCancelled()
        if p:
            return Path(p)
        print("Chemin vide.\n")


def ask_int(prompt, min_value=None, max_value=None, allow_quit=False):
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
    project_root = Path(__file__).resolve().parents[2]
    return (project_root / "automata_files" / f"a{choice}.txt").resolve()