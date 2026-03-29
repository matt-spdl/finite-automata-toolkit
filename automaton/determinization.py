from automaton.automaton_class import Automaton

def is_determinist(automate):
    """
    Vérifie si l'automate est déterministe.

    Args:
        automate : l'automate à vérifier.

    Returns:
        True si l'automate est déterministe, False sinon.
    """
    # Il doit avoir une seule entrée
    if len(automate.initial_states) != 1:
        return False

    # Aucune transition multiple pour un même caractère et pas de transitions epsilon
    for etat in automate.transitions:
        for symbole in automate.transitions[etat]:
            if symbole == '#':
                return False  # La simple présence d'un epsilon rend l'automate non déterministe
            if len(automate.transitions[etat][symbole]) > 1:
                return False
    return True


def formate_name_state(liste_etats):
    """
    Formate un nom d'état composé à partir d'une liste d'états.

    Args:
        liste_etats : la liste des états à fusionner.

    Returns:
        Une chaîne de caractères représentant l'état composé (ex : "0.1.2").
    """
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
    Fonction universelle de déterminisation

    1. Vérification préalable : S'assure que l'automate fourni n'est pas déjà
       déterministe, sinon lève une erreur.

    2. Initialisation et État initial : Crée l'AD et définit comme unique état initial
       l'ensemble des états initiaux de l'AND, en y incluant leur
       epsilon-fermeture.

    3. Création des états composés : Construit dynamiquement les nouveaux états de l'AD,
       qui sont de façon naturelle des ensembles constitués en états de l'AND d'origine.
       L'algorithme utilise une file d'attente pour traiter ces nouveaux états un par un.

    4. Identification des sorties : Marque un état composé comme terminal s'il
       contient au moins un état terminal de l'automate d'origine.

    5. Calcul des transitions : Pour chaque état composé traité et pour chaque caractère
       de l'alphabet, l'algorithme met ensemble les cibles de ses composantes pour créer la nouvelle transition.

    6. Condition d'arrêt : Le processus itératif s'arrête de lui-même car la boucle
       se termine lorsqu'aucun nouvel état n'apparait.
    """
    # On ne déterminise pas un automate déjà déterministe
    if is_determinist(and_origine):
        raise ValueError("L'automate est déjà déterministe")


    ad_final = Automaton(and_origine.name)

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