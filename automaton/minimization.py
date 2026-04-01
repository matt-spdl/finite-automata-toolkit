# Mathias
from automaton.determinization import is_determinist
from automaton.completion import is_complete
from automaton.automaton_class import Automaton


def split_terminal_nonterminal_states(automaton: Automaton):
    """
    Sépare les états en deux groupes :
    - états terminaux
    - états non terminaux
    """
    non_terminal_group = {}
    terminal_group = {}

    for source_state, transitions in automaton.transitions.items():
        for symbol, targets in transitions.items():

            if source_state not in automaton.final_states:
                if source_state not in non_terminal_group:
                    non_terminal_group[source_state] = {}

                if symbol not in non_terminal_group[source_state]:
                    non_terminal_group[source_state][symbol] = set()

                for target in targets:
                    if target not in automaton.final_states:
                        non_terminal_group[source_state][symbol].add("NT")
                    else:
                        non_terminal_group[source_state][symbol].add("T")

            else:
                if source_state not in terminal_group:
                    terminal_group[source_state] = {}

                if symbol not in terminal_group[source_state]:
                    terminal_group[source_state][symbol] = set()

                for target in targets:
                    if target not in automaton.final_states:
                        terminal_group[source_state][symbol].add("NT")
                    else:
                        terminal_group[source_state][symbol].add("T")

    return non_terminal_group, terminal_group


def group_states_by_transition_signature(automaton: Automaton, state_group):
    """
    Regroupe les états ayant les mêmes signatures de transitions
    """
    grouped_result = {}
    signature_map = {}
    group_index = 1

    for source_state, transitions_signature in state_group.items():
        signature_str = str(transitions_signature)

        if signature_str not in signature_map:
            signature_map[signature_str] = []

        signature_map[signature_str].append(source_state)

    for states_list in signature_map.values():
        grouped_result[group_index] = states_list
        group_index += 1

    return grouped_result


def merge_terminal_and_nonterminal_groups(non_terminal_groups, terminal_groups):
    """
    Fusionne les groupes terminaux et non terminaux
    """
    merged_groups = {}

    for states_list in non_terminal_groups.values():
        merged_groups[states_list[0]] = states_list

    for states_list in terminal_groups.values():
        merged_groups[states_list[0]] = states_list

    return merged_groups


def classify_states_by_target_group(automaton: Automaton, current_groups):
    """
    Associe chaque état à la classe de ses états cibles
    """
    state_classification = {}

    for source_state, transitions in automaton.transitions.items():
        for symbol, targets in transitions.items():

            if source_state not in state_classification:
                state_classification[source_state] = {}

            if symbol not in state_classification[source_state]:
                state_classification[source_state][symbol] = set()

            for target in targets:
                for group_id, group_states in current_groups.items():
                    if target in group_states:
                        state_classification[source_state][symbol] = group_id

    return state_classification


def remove_equivalent_duplicate_states(classified_states, current_groups):
    """
    Supprime les états équivalents (mêmes transitions et même groupe)
    """
    minimized_dict = {}
    minimized_signature = {}
    seen_signatures = []

    for group_id in current_groups:
        for state, signature in classified_states.items():

            if state in current_groups[group_id]:
                if signature not in seen_signatures:

                    if state not in minimized_dict:
                        minimized_dict[state] = []

                    minimized_dict[state].append(signature)
                    minimized_signature[state] = signature

                    seen_signatures.append(signature)

        seen_signatures = []

    return minimized_dict, minimized_signature


def refine_partitions(minimized_signature, classified_states, current_groups):
    """
    Raffine les classes (partitionnement)
    """
    refined_groups = {}

    for state, signature in minimized_signature.items():
        for state2, signature2 in classified_states.items():
            for group_id, group_states in current_groups.items():

                if signature2 == signature and state2 in group_states and state in group_states:
                    if str(state) not in refined_groups:
                        refined_groups[str(state)] = []

                    refined_groups[str(state)].append(state2)

    return refined_groups


def build_minimized_automaton(automaton: Automaton, minimized_groups):
    """
    Reconstruit l'automate minimisé
    """
    minimized_automaton = Automaton(automaton.name)

    for new_state, signatures in minimized_groups.items():
        for signature in signatures:
            for symbol, target in signature.items():

                minimized_automaton.add_transition(new_state, symbol, target)

                if new_state in automaton.initial_states:
                    minimized_automaton.add_initial_state(new_state)

                if new_state in automaton.final_states:
                    minimized_automaton.add_final_state(new_state)

    return minimized_automaton


def Minimization(automaton: Automaton):
    """
    Fonction principale de minimisation
    """

    if not is_determinist(automaton):
        raise ValueError(f"L'automate {automaton.name} n'est pas déterministe")

    if not is_complete(automaton):
        raise ValueError(f"L'automate {automaton.name} n'est pas complet")

    non_terminal_group, terminal_group = split_terminal_nonterminal_states(automaton)

    non_terminal_group = group_states_by_transition_signature(automaton, non_terminal_group)
    terminal_group = group_states_by_transition_signature(automaton, terminal_group)

    current_groups = merge_terminal_and_nonterminal_groups(non_terminal_group, terminal_group)

    classified_states = classify_states_by_target_group(automaton, current_groups)

    minimized_dict, minimized_signature = remove_equivalent_duplicate_states(
        classified_states, current_groups
    )

    while len(minimized_dict) != len(current_groups):
        current_groups = refine_partitions(minimized_signature, classified_states, current_groups)

        classified_states = classify_states_by_target_group(automaton, current_groups)

        minimized_dict, minimized_signature = remove_equivalent_duplicate_states(
            classified_states, current_groups
        )

    result = build_minimized_automaton(automaton, minimized_dict)

    if result == automaton:
        print("L'automate était déjà minimal.")

    return result


if __name__ == "__main__":
    from automaton.file_manager import read_automaton_from_file

    automaton = read_automaton_from_file(
        "C:/Users/matte/dev/finite-automata-toolkit/automata_files/a44.txt"
    )

    print(automaton)

    minimized_automaton = Minimization(automaton)

    print(minimized_automaton)