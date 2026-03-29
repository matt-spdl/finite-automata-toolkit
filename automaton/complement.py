# Louis
from automaton import is_determinist, is_complete
from automaton.automaton_class import Automaton
from automaton.determinization import determinize
from automaton.completion import completion

def complementarization(automaton : Automaton):
    """
    Calcule l'automate complémentaire de l'automate donné.
    L'automate doit être déterministe et complet avant d'appeler cette fonction.

    Args:
        automaton : l'automate dont on veut le complémentaire.

    Returns:
        Un nouvel automate dont les états finaux sont les états non-finaux de l'automate d'origine.
    """

    # On utilise un automate Déterministe et Complet pour cette fonction
    if not is_determinist(automaton):
        raise ValueError(f"L'automate {automaton.name} n'est pas déterministe")
    else :
        if not is_complete(automaton):
            raise ValueError(f"L'automate {automaton.name} n'est pas complet")
        else :
            # On crée un nouvel automate pour le complémentaire
            comp_automaton = Automaton()

            # On copie les états et les transitions dans ce nouvel automate
            for state in automaton.states :
                comp_automaton.add_state(state)

                # On inverse les états finaux de l'automate
                if state not in automaton.final_states:
                    comp_automaton.add_final_state(state)

            for state in automaton.states:
                transitions = automaton.get_transitions_from_state(state)
                for symbol in transitions:
                    for target in transitions[symbol]:
                        comp_automaton.add_transition(state, symbol, target)

            # On copie les états initiaux
            for initial in automaton.initial_states :
                comp_automaton.add_initial_state(initial)

            # On obtient l'automate complémentaire de celui donné en entrée
            return comp_automaton


if __name__ == "__main__":

    from .file_manager import read_automaton_from_file

    automaton = read_automaton_from_file("C:/Users/Louis/PycharmProjects/finite-automata-toolkit/automata_files/automate.exemple.txt")
    print(automaton)
    d_automaton = determinize(automaton)
    print(d_automaton)
    dc_automaton = completion(d_automaton)
    print(dc_automaton)
    cmp_automaton = complementarization(dc_automaton)
    print(cmp_automaton)