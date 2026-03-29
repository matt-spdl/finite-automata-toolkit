# Bastien
# Est déterminisé
# Est complet
# Est Standard

def is_deterministic(automate):
    if len(automate.initial_states) != 1:
        return False
    for etat in automate.transitions:
        for symbole in automate.transitions[etat]:
            if len(automate.transitions[etat][symbole]) > 1:
                return False
    return True

def is_complete (automate):
    for i in automate.states:
        if i not in automate.transitions:
            return False
        for j in automate.alphabet:
            if j not in automate.transitions[i]:
                return False
    return True

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