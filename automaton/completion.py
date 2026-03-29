# Bastien
from automaton import Automaton


def is_complete (automate):
    for i in automate.states:
        if i not in automate.transitions:
            return False
        for j in automate.alphabet:
            if j not in automate.transitions[i]:
                return False
    return True

def completion (old_automaton):
    """
            make a complete version of the automaton given.

            Args:
                old_automaton : the automaton we want to complete
    """
    if is_complete(old_automaton):
        return old_automaton
    "copie de l'automate"
    new_automaton = old_automaton.copy()

    "ajout de la poubelle"
    new_automaton.add_state("P")

    "parcours des états"
    for i in new_automaton.states:

        "parcours de l'alphabet, et donc des sorties de chaque état"
        for j in new_automaton.alphabet:

            "ajout des transitions manquantes"
            if i not in new_automaton.transitions:
                new_automaton.add_transition(i,j,"P")
            elif j not in new_automaton.transitions[i]:
                new_automaton.add_transition(i,j,"P")

    return new_automaton