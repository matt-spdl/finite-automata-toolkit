# Louis
from automaton.automaton_class import Automaton

def is_standard (automate):
    """vérifie si l'automate donné en paramètre possède seulement 1 état initial et aucune transition dans cet état"""
    if len(automate.initial_states)>1:
        return False
    for i in automate.transitions:
        for j in automate.transitions[i]:
            for k in automate.transitions[i][j]:
                if k in automate.initial_states:
                    return False
    return True

def standardization(automaton : Automaton ):
    """
    Standardise l'automate donné : crée un unique état initial "Es" sans transitions entrantes.
    Si l'automate est déjà standardisé, une exception est levée.

    Args:
        automaton : l'automate à standardiser.

    Returns:
        Un nouvel automate standardisé.

    Raises:
        ValueError : si l'automate est déjà standardisé.
    """
    if is_standard(automaton):
        raise ValueError(f"L'automate {automaton.name} est déjà standardisé")
    else:
        # Copie des états et transitions dans le nouvel automate
        std_automaton = Automaton()

        for state in automaton.states :
            std_automaton.add_state(state)

        for state in automaton.final_states :
            std_automaton.add_final_state(state)

        for state in automaton.states :
            transitions = automaton.get_transitions_from_state(state)
            for symbol in transitions :
                for target in transitions[symbol] :
                    std_automaton.add_transition(state,symbol,target)

        # Création d'un nouvel état initial
        new_initial = "Es"

        std_automaton.add_initial_state(new_initial)

        # Copie des transitions des anciens états initiaux vers le nouveau
        for old_init in automaton.initial_states :
            transitions = automaton.get_transitions_from_state(old_init)

            for symbol in transitions :
                for target in transitions[symbol] :
                    std_automaton.add_transition(new_initial, symbol, target)

            # On regarde si l'ancien état était dans les états finaux
            # S'il l'est, le nouveau doit l'être aussi.
            if old_init in automaton.final_states:
                std_automaton.add_final_state(new_initial)


    return std_automaton