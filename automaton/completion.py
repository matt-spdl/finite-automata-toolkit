# Bastien
from automaton.automaton import *

def completion (old_automaton):

    "copie de l'automate"
    new_automaton = Automaton()
    "je me rend compte que la première boucle est pas forcèment utile... Mais on sait jamais"
    for i in old_automaton.states :
        new_automaton.add_state(i)
    for i in old_automaton.alphabet :
        new_automaton.alphabet.add(i)
    for i in old_automaton.initial_states:
        new_automaton.add_initial_state(i)
    for i in old_automaton.final_states:
        new_automaton.add_final_state(i)
    for i in old_automaton.transitions:
        for j in old_automaton.transitions[i]:
            for k in old_automaton.transitions[i][j]:
                new_automaton.add_transition(i,j,k)

    "ajout de la poubelle"
    new_automaton.add_state("P")
    for i in new_automaton.states:
        for j in new_automaton.alphabet:
            if i not in new_automaton.transitions:
                new_automaton.add_transition(i,j,"P")
            elif j not in new_automaton.transitions[i]:
                new_automaton.add_transition(i,j,"P")

    return new_automaton