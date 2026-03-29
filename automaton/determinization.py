from automaton import Automaton

def is_determinist(automate):
    # Il doit avoir une seule entrée
    if len(automate.initial_states) != 1:
        return False

        # Aucune transition multiple pour un même caractère et pas de transitions epsilon
    for etat in automate.transitions:
        for symbole in automate.transitions[etat]:
            if symbole == 'epsilon':
                return False  # La simple présence d'un epsilon rend l'automate non déterministe
            if len(automate.transitions[etat][symbole]) > 1:
                return False
    return True


def formate_name_state(liste_etats):
    # On trie et on joint les noms d'états pour former l'état composé.
    return ".".join(sorted(str(e) for e in set(liste_etats)))


def get_epsilon_closure(automate, etats_liste):
    """
    Calcule l'ensemble des états atteignables via des transitions epsilon (ou '#' / 'epsilon')
    Si l'automate n'a pas d'epsilon, cela retourne simplement la liste de départ.
    """
    fermeture = set(etats_liste)
    pile = list(etats_liste)

    while pile:
        etat = pile.pop()
        # Vérifie si l'état possède des transitions 'epsilon'
        if etat in automate.transitions and '#' in automate.transitions[etat]:
            for cible in automate.transitions[etat]['#']:
                if cible not in fermeture:
                    fermeture.add(cible)
                    pile.append(cible)

    return sorted(list(fermeture))


def get_symbol_transitions(automate, etats_liste, symbole):
    """
    Récupère toutes les cibles atteignables depuis un groupe d'états pour un symbole donné,
    PUIS applique la fermeture epsilon sur ces cibles.
    """
    cibles_directes = set()
    for etat in etats_liste:
        # On récupère les états cibles pour le symbole lu
        if etat in automate.transitions and symbole in automate.transitions[etat]:
            cibles_directes.update(automate.transitions[etat][symbole])

    # On retourne la fermeture epsilon de toutes ces cibles
    return get_epsilon_closure(automate, list(cibles_directes))


def determinize(and_origine):
    """
    Fonction universelle de déterminisation pure (sans complétion)
    """
    # On ne déterminise pas un automate déjà déterministe
    if is_determinist(and_origine):
        raise ValueError("L'automate est déjà déterministe")


    ad_final = Automaton()

    # L'alphabet final est celui d'origine, moins le symbole 'epsilon' s'il existe
    ad_final.alphabet = {sym for sym in and_origine.alphabet if sym != '#'}

    # Calcul de l'état initial
    etat_initial_liste = get_epsilon_closure(and_origine, and_origine.initial_states)
    nom_initial = formate_name_state(etat_initial_liste)
    ad_final.add_initial_state(nom_initial)

    file_attente = [etat_initial_liste]
    explores_noms = set()

    # Boucle de construction des nouveaux états
    while file_attente:
        courant_liste = file_attente.pop(0)
        nom_courant = formate_name_state(courant_liste)

        if nom_courant in explores_noms:
            continue

        explores_noms.add(nom_courant)

        # Définition de l'état terminal
        est_final = any(e in and_origine.final_states for e in courant_liste)
        if est_final:
            ad_final.add_final_state(nom_courant)
        else:
            ad_final.add_state(nom_courant)

        # Calcul des transitions pour chaque symbole du nouvel alphabet
        for symbole in sorted(ad_final.alphabet):
            # Utilisation de notre sous-fonction qui gère directement cibles + epsilons
            prochain_ensemble = get_symbol_transitions(and_origine, courant_liste, symbole)

            # Si prochain_ensemble est vide, le bloc if n'est pas exécuté.
            # Aucune transition n'est créée vers le vide, ce qui évite la complétion forcée.
            if prochain_ensemble:
                nom_prochain = formate_name_state(prochain_ensemble)
                ad_final.add_transition(nom_courant, symbole, nom_prochain)

                if nom_prochain not in explores_noms:
                    file_attente.append(prochain_ensemble)

    return ad_final