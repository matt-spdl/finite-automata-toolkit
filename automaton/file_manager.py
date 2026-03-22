from pathlib import Path
from automaton import Automaton

def _read_lines(path):
    """Lit le fichier et retourne les lignes sous forme de tableaux."""
    with open(path, "r", encoding="utf-8") as file:
        lines = []
        for line in file.readlines():
            tokens = line.strip().split()
            if tokens:
                lines.append(tokens)
    return lines


def _read_symbols_line(tokens, filename):
    """Ligne 1 : symboles de l’alphabet."""
    if not tokens:
        raise ValueError(f"Format invalide : {filename}. L’alphabet est vide.")
    return set(tokens)


def _read_states_line(tokens, filename, line_number, description):
    """Lit une ligne contenant une liste d'états."""
    if not tokens:
        raise ValueError(
            f"Format invalide : {filename}, ligne {line_number}. "
            f"{description} manquant."
        )
    return set(tokens)


def _read_transition(tokens, filename, line_number, alphabet):
    """Valide le format et retourne une transition."""
    if len(tokens) != 3:
        raise ValueError(
            f"Format invalide : {filename}, ligne {line_number}. "
            f"Une transition doit être : <source> <symbole> <cible>."
        )

    source, symbol, target = tokens

    if symbol not in alphabet:
        raise ValueError(
            f"Format invalide : {filename}, ligne {line_number}. "
            f"Symbole '{symbol}' non présent dans l’alphabet."
        )

    return source, symbol, target


def read_automaton_from_file(filename) -> Automaton:
    """
    Lit un automate à partir d’un fichier texte et retourne une instance d’Automaton.
    Le fichier doit respecter le format suivant :
    - Ligne 1 : symboles de l’alphabet (séparés par des espaces)
    - Ligne 2 : états initiaux (séparés par des espaces)
    - Ligne 3 : états finaux (séparés par des espaces)
    - Lignes suivantes : transitions au format <source> <symbole> <cible>
    """
    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(f"Fichier introuvable : {filename}")

    if path.suffix != ".txt":
        raise ValueError(f"Format invalide : {filename}. Fichier .txt attendu.")

    lines = _read_lines(path)

    if len(lines) < 3:
        raise ValueError(
            f"Format invalide : {filename}. "
            f"Au moins 3 lignes sont attendues."
        )

    automaton = Automaton()

    # Ligne 1 : alphabet
    alphabet = _read_symbols_line(lines[0], filename)

    # Ligne 2 : états initiaux
    initial_states = _read_states_line(
        lines[1], filename, 2, "État initial"
    )
    for state in initial_states:
        automaton.add_initial_state(state)

    # Ligne 3 : états finaux
    final_states = _read_states_line(
        lines[2], filename, 3, "État final"
    )
    for state in final_states:
        automaton.add_final_state(state)

    # Transitions
    for i in range(3, len(lines)):
        source, symbol, target = _read_transition(
            lines[i], filename, i + 1, alphabet
        )
        automaton.add_transition(source, symbol, target)

    return automaton

if __name__ == "__main__":
    # Exemple
    automaton = read_automaton_from_file("../automata_files/automate.exemple.txt")
    print(automaton)