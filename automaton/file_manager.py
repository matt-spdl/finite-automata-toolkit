from pathlib import Path
from .automaton_class import Automaton

FILE_MIN_LINE_NUMBER = 4

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
        Ligne 1 : nom de l'automate
        Ligne 2 : liste des symboles de l’alphabet séparés par des espaces.
        Ligne 3 : indices des états initiaux séparés par des espaces.
        Ligne 4 : indices des états finaux séparés par des espaces.
        Lignes 5 et suivantes : transitions sous la forme
            <état de départ> <symbole> <état d’arrivée>
    """
    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(f"Fichier introuvable : {filename}")

    if path.suffix != ".txt":
        raise ValueError(f"Format invalide : {filename}. Fichier .txt attendu.")

    lines = _read_lines(path)

    if len(lines) < FILE_MIN_LINE_NUMBER:
        raise ValueError(
            f"Format invalide : {filename}. "
            f"Au moins {FILE_MIN_LINE_NUMBER} lignes sont attendues."
        )

    # Ligne 1 : nom
    name = " ".join(lines[0])
    automaton = Automaton(name)

    # Ligne 2 : alphabet
    alphabet = _read_symbols_line(lines[1], filename)
    for symbol in alphabet:
        automaton.add_symbol(symbol)

    # Ligne 3 : états initiaux
    initial_states = _read_states_line(
        lines[2], filename, 3, "État initial"
    )
    for state in initial_states:
        automaton.add_initial_state(state)

    # Ligne 4 : états finaux
    final_states = _read_states_line(
        lines[3], filename, 4, "État final"
    )
    for state in final_states:
        automaton.add_final_state(state)

    # Transitions
    for i in range(FILE_MIN_LINE_NUMBER, len(lines)):
        source, symbol, target = _read_transition(
            lines[i], filename, i + 1, alphabet
        )
        automaton.add_transition(source, symbol, target)

    return automaton

if __name__ == "__main__":
    # Exemple
    a = read_automaton_from_file("C:/Users/matte/dev/finite-automata-toolkit/automata_files/a44.txt")
    print(a)