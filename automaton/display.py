from automaton.automaton_class import Automaton
from automaton.file_manager import read_automaton_from_file

CELL_SIZE = 10
CELL_SIZE_STATE_TYPE = 5
EMPTY_TRANSITION = "--"

def _format_cell(value: str, cell_size: int) -> str:
    """Formate une valeur dans une cellule de largeur fixe."""
    return str(value).ljust(cell_size)

def _format_transition(next_states) -> str:
    """
    Formate les états cibles d'une transition pour l'affichage.

    Args:
        next_states : les états cibles de la transition.

    Returns:
        Une chaîne avec les états séparés par des virgules, ou "--" si aucun état.
    """
    # Si pas d'état suivant, on affiche le symbole par défaut
    if not next_states:
        return EMPTY_TRANSITION

    # Sinon on concatène les états cibles
    return ",".join(str(state) for state in next_states)

def _get_state_type(state: str, automaton: Automaton) -> str:
    """
    Retourne le type d'un état : "E" (initial), "S" (final), "E/S" (les deux) ou "" (aucun).

    Args:
        state : le nom de l'état.
        automaton : l'automate contenant l'état.

    Returns:
        Une chaîne indiquant le type de l'état.
    """
    types = []
    if automaton.is_initial_state(state):
        types.append("E")
    if automaton.is_final_state(state):
        types.append("S")
    # Retourne "", "E", "S" ou "E/S" selon le cas
    return "/".join(types)

def _format_header(alphabet, cell_size: int) -> str:
    """
    Crée la ligne d'en-tête du tableau de l'automate.

    Args:
        alphabet : les symboles de l'alphabet.
        cell_size : la largeur de chaque colonne.

    Returns:
        Une chaîne formatée représentant l'en-tête du tableau.
    """
    # Crée la première ligne du tableau :
    # - première colonne : type d'état
    # - deuxième colonne : nom de l'état
    # - colonnes suivantes : symboles de l'alphabet
    row = []
    row.append(_format_cell("", CELL_SIZE_STATE_TYPE))
    row.append(_format_cell("État", cell_size))

    # Ajoute une colonne pour chaque symbole de l'alphabet
    for symbol in alphabet:
        row.append(_format_cell(symbol, cell_size))

    return "".join(row)

def _format_row(state: str, automaton: Automaton, cell_size: int) -> str:
    """
    Crée la ligne du tableau correspondant à un état donné.

    Args:
        state : le nom de l'état.
        automaton : l'automate contenant l'état.
        cell_size : la largeur de chaque colonne.

    Returns:
        Une chaîne formatée représentant la ligne de l'état dans le tableau.
    """
    # Crée une ligne du tableau pour un état {state} donné
    row = []
    row.append(_format_cell(_get_state_type(state, automaton), CELL_SIZE_STATE_TYPE))
    row.append(_format_cell(state, cell_size))

    # Pour chaque symbole, récupère les états accessibles depuis l'état courant
    for symbol in automaton.alphabet:
        next_states = automaton.get_target_states(state, symbol)
        row.append(_format_cell(_format_transition(next_states), cell_size))

    return "".join(row)

def get_min_cell_size(states) -> int:
    """Calcule la taille de cellule nécessaire pour afficher correctement les états de l'automate."""
    max_state_length = max(len(state) for state in states)
    max_state_length += 2
    return max(CELL_SIZE, max_state_length)


def get_automaton_table(automaton: Automaton) -> list[str]:
    """
    Renvoie un tableau de lignes formatées représentant l'automate.
    Chaque élément de la liste correspond à une ligne du tableau.
    """
    table = []
    cell_size = get_min_cell_size(automaton.states)

    # Ajoute l'en-tête
    header = _format_header(automaton.alphabet, cell_size)
    table.append(header)

    # Ajoute les lignes pour chaque état
    for state in automaton.states:
        row = _format_row(state, automaton, cell_size)
        table.append(row)

    return table

def display_automaton_table(automaton: Automaton) -> None:
    """
    Affiche le tableau de l'automate dans la console.

    Args:
        automaton : l'automate à afficher.
    """
    print(f"Nom : {automaton.name}")
    # Affiche d'abord l'en-tête puis toutes les lignes de l'automate
    table = get_automaton_table(automaton)
    for line in table:
        print(line)

if __name__ == "__main__":
    automaton = read_automaton_from_file("../automata_files/automate.exemple.txt")
    display_automaton_table(automaton)
    print(get_automaton_table(automaton))