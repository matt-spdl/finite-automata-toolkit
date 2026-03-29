# Bastien
from automaton import Automaton

def completion (old_automaton):
    """
            make a complete version of the automaton given.

            Args:
                old_automaton : the automaton we want to complete
    """

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