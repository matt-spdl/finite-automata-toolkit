from automaton import Automaton
from file_manager import read_automaton_from_file

CELL_SIZE = 10
CELL_SIZE_STATE_TYPE = 5
EMPTY_TRANSITION = "--"

def _format_cell(value: str, cell_size: int) -> str:
    return str(value).ljust(cell_size)

def _format_transition(next_states) -> str:
    # Si pas d'état suivant, on affiche le symbole par défaut
    if not next_states:
        return EMPTY_TRANSITION

    # Sinon on concatène les états cibles
    return ",".join(str(state) for state in next_states)

def _get_state_type(state: str, automaton: Automaton) -> str:
    types = []
    if automaton.is_initial_state(state):
        types.append("E")
    if automaton.is_final_state(state):
        types.append("S")
    # Retourne "", "E", "S" ou "E/S" selon le cas
    return "/".join(types)

def _display_header(alphabet, cell_size: int) -> None:
    # Crée la première ligne du tableau :
    # - première colonne : type d'état
    # - deuxième colonne : nom de l'état
    # - colonnes suivantes : symboles de l'alphabet
    row = [
        _format_cell("", CELL_SIZE_STATE_TYPE),
        _format_cell("État", cell_size),
    ]

    # Ajoute une colonne pour chaque symbole de l'alphabet
    for symbol in alphabet:
        row.append(_format_cell(symbol, cell_size))

    print("".join(row))

def _display_row(state: str, automaton: Automaton, cell_size: int) -> None:
    # Crée une ligne du tableau pour un état {state} donné
    row = [
        _format_cell(
            _get_state_type(state, automaton),
            CELL_SIZE_STATE_TYPE
        ),
        _format_cell(state, cell_size),
    ]

    # Pour chaque symbole, récupère les états accessibles depuis l'état courant
    for symbol in automaton.alphabet:
        next_states = automaton.get_target_states(state, symbol)
        row.append(
            _format_cell(_format_transition(next_states),
            cell_size)
        )

    print("".join(row))

def _display_rows(automaton: Automaton, cell_size: int) -> None:
    # Affiche une ligne pour chaque état de l'automate
    for state in automaton.states:
        _display_row(state, automaton, cell_size)

def display_automaton_table(automaton: Automaton) -> None:
    # Affiche d'abord l'en-tête puis toutes les lignes de l'automate
    _display_header(automaton.alphabet, CELL_SIZE)
    _display_rows(automaton, CELL_SIZE)

if __name__ == "__main__":
    automaton = read_automaton_from_file("../automata_files/automate.exemple.txt")
    display_automaton_table(automaton)