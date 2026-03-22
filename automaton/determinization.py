# Thomas
from automaton import Automaton

def est_deterministe(automate):
    if len(automate.initial_states) != 1:
        return False
    for etat in automate.transitions:
        for symbole in automate.transitions[etat]:
            if len(automate.transitions[etat][symbole]) > 1:
                return False
    return True


def formater_nom_etat(liste_etats):
    return ".".join(sorted(str(e) for e in set(liste_etats)))


def determiniser(and_origine):
    if est_deterministe(and_origine):
        return and_origine

    ad_final = Automaton()
    ad_final.alphabet = set(and_origine.alphabet)

    etat_initial_liste = sorted(list(and_origine.initial_states))
    nom_initial = formater_nom_etat(etat_initial_liste)
    ad_final.add_initial_state(nom_initial)

    file_attente = [etat_initial_liste]
    explores_noms = set()

    while file_attente:
        courant_liste = file_attente.pop(0)
        nom_courant = formater_nom_etat(courant_liste)

        if nom_courant in explores_noms:
            continue

        explores_noms.add(nom_courant)

        est_final = False
        for e in courant_liste:
            if e in and_origine.final_states:
                est_final = True
                break

        if est_final:
            ad_final.add_final_state(nom_courant)
        else:
            ad_final.add_state(nom_courant)

        for symbole in sorted(and_origine.alphabet):
            prochain_ensemble = set()
            for etat in courant_liste:
                cibles = and_origine.get_target_states(etat, symbole)
                prochain_ensemble.update(cibles)

            if prochain_ensemble:
                prochain_liste = sorted(list(prochain_ensemble))
                nom_prochain = formater_nom_etat(prochain_liste)
                ad_final.add_transition(nom_courant, symbole, nom_prochain)

                if nom_prochain not in explores_noms:
                    file_attente.append(prochain_liste)

    return ad_final
