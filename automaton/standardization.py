# Louis

from automaton import Automaton
from properties import is_standard

def standardization(automaton : Automaton ):
    if is_standard(automaton):
        return automaton
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


if __name__ == "__main__":

    from file_manager import read_automaton_from_file

    automaton = read_automaton_from_file("C:/Users/Louis/PycharmProjects/finite-automata-toolkit/automata_files/automate.exemple.txt")
    print(automaton)
    n_automaton = standardization(automaton)
    print(n_automaton)
