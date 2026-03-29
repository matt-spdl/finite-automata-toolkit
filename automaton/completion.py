# Bastien
from automaton.automaton_class import Automaton

def is_complete(automate: Automaton):
    """
    Vérifie si l'automate est complet, c'est-à-dire si chaque état possède
    une transition pour chaque symbole de l'alphabet.

    Args:
        automate : l'automate à vérifier.

    Returns:
        True si l'automate est complet, False sinon.
    """
    for i in automate.states:
        if i not in automate.transitions:
            return False
        for j in automate.alphabet:
            if j not in automate.transitions[i]:
                return False
    return True

def completion(old_automaton: Automaton):
    """
    Retourne une version complète de l'automate donné.
    Si l'automate est déjà complet, il est retourné tel quel.

    Args:
        old_automaton : l'automate à compléter.

    Returns:
        Un nouvel automate complet (avec état poubelle si nécessaire).
    """
    if is_complete(old_automaton):
        return old_automaton
    # Copie de l'automate
    new_automaton = old_automaton.copy()

    # Ajout de l'état poubelle
    new_automaton.add_state("P")

    # Parcours des états
    for i in new_automaton.states:

        # Parcours de l'alphabet, et donc des sorties de chaque état
        for j in new_automaton.alphabet:

            # Ajout des transitions manquantes vers l'état poubelle
            if i not in new_automaton.transitions:
                new_automaton.add_transition(i, j, "P")
            elif j not in new_automaton.transitions[i]:
                new_automaton.add_transition(i, j, "P")

    return new_automaton