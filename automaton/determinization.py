# Thomas
from automaton import Automaton

def is_determinist(automate):
    if len(automate.initial_states) != 1:
        return False  #On regarde s'il y a plusieurs états d'entrées
    for etat in automate.transitions:
        for symbole in automate.transitions[etat]:
            if len(automate.transitions[etat][symbole]) > 1:  #On regarde si à partir d'un état, plusieurs flèches avec la même lettre sortent
                return False
    return True


def formate_name_state(liste_etats):
    return ".".join(sorted(str(e) for e in set(liste_etats)))  #On join le nom  des états pour en former qu'un seul


def determinize(and_origine):
    if is_determinist(and_origine):  #Avant de déterminiser, on check si l'automate n'est pas déjà déterministe
        raise ValueError ("L'automate est déjà déterministe")

    ad_final = Automaton()
    ad_final.alphabet = set(and_origine.alphabet) #Initialisation du nouvel automate déterministe

    etat_initial_liste = sorted(list(and_origine.initial_states))  #L'unique état initial de l'AD est l'ensemble des états initiaux de l'AND d'origine
    nom_initial = formate_name_state(etat_initial_liste)
    ad_final.add_initial_state(nom_initial)

    file_attente = [etat_initial_liste]  #File pour traiter les nouveaux états composés et set pour éviter les boucles infinies
    explores_noms = set()

    while file_attente:
        courant_liste = file_attente.pop(0)   #On récupère le prochain groupe d'états à traiter
        nom_courant = formate_name_state(courant_liste)

        if nom_courant in explores_noms:  #Si cet état composé a déjà été traité, on passe au suivant
            continue

        explores_noms.add(nom_courant)

        est_final = False   #Un état composé est terminal s'il contient au moins un état terminal de l'AND
        for e in courant_liste:
            if e in and_origine.final_states:
                est_final = True
                break

        if est_final:
            ad_final.add_final_state(nom_courant)
        else:
            ad_final.add_state(nom_courant)

        for symbole in sorted(and_origine.alphabet):  #Pour chaque symbole, on cherche où vont les états du groupe
            prochain_ensemble = set()
            for etat in courant_liste:
                cibles = and_origine.get_target_states(etat, symbole)  #On cumule toutes les cibles possibles pour ce symbole
                prochain_ensemble.update(cibles)

            if prochain_ensemble:  #Si des transitions existent, on crée le nouvel état composé
                prochain_liste = sorted(list(prochain_ensemble))
                nom_prochain = formate_name_state(prochain_liste)
                ad_final.add_transition(nom_courant, symbole, nom_prochain)  #On ajoute la transition unique dans l'AD

                if nom_prochain not in explores_noms:  #Si ce nouvel état n'a jamais été vu, on l'ajoute à la file d'attente
                    file_attente.append(prochain_liste)

    return ad_final
