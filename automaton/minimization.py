# Mathias
from automaton.determinization import is_determinist
from automaton.completion import is_complete
from automaton.automaton_class import Automaton

def separationTerminal(automaton):
    """
    Sépare les états dans deux dictionnaires
    Un dictionnaire qui regroupe tous les états terminaux avec leur cible sur des états terminaux ou non
    Un dictionnaire qui regroupe tous les états non-terminaux avec leur cible sur des états terminaux ou non

    Args:
        un automate

    Returns:
        Deux dictionnaires de dictionnaire
    """
    Group_NT = {}
    Group_T = {}
    for source, transitions in automaton.transitions.items():
        for symbol, targets in transitions.items():
            if source not in automaton.final_states:
                if source not in Group_NT:
                    Group_NT[source] = {}
                if symbol not in Group_NT[source]:
                    Group_NT[source][symbol] = set()
                for target in targets:
                    if target not in automaton.final_states:
                        Group_NT[source][symbol].add("NT")
                    else :
                        Group_NT[source][symbol].add("T")
            else :
                if source not in Group_T:
                    Group_T[source] = {}
                if symbol not in Group_T[source]:
                    Group_T[source][symbol] = set()
                for target in targets:
                    if target not in automaton.final_states:
                        Group_T[source][symbol].add("NT")
                    else:
                        Group_T[source][symbol].add("T")
    return Group_NT, Group_T


def regroup(automaton, Group):
    """
    Regroupe les états terminaux (ou non) qui ont des cibles terminales ou non identiques

    Args:
        Un automate et un dictionnaire de dictionnaire

    Returns:
        Un dictionnaire qui contient des listes en valeurs
    """
    result = {}
    compar = {}
    i = 1
    for source,values in Group.items():

        verif = str(values)
        if verif not in compar:
            compar[verif] = []
        compar[verif].append(source)

    for verif in compar.values():
        result[i]=verif
        i += 1
    return result

def assemble(Group_NT, Group_T):
    """
    Assemble les deux dictionnaires de listes des états terminaux et des états non-terminaux.

    Args:
        deux dictionnaires avec des listes en valeurs

    Returns:
        un dictionnaire avec des listes en valeurs
    """
    result ={}
    i = 1

    for values in Group_NT.values():
        result[values[0]] = values
        i += 1

    for values in Group_T.values():
        result[values[0]] = values
        i += 1

    return result

def classification(automaton, reGroup):
    """
    La fonction crée des classes (groupes) avec les groupes précédents formées
    et regroupe  dans un dictionnaire, tous les états de l'automates avec la classe de leur cible

    Args:
        Un dictionnaire, un dictionnaire avec des listes en valeurs

    Returns:
        Un dictionnaire contenant un dictionnaire en valeur dans un set
    """
    result = {}
    for source, transitions in automaton.transitions.items():
        for symbol, targets in transitions.items():
            if source not in result:
                result[source] = {}
            if symbol not in result[source]:
                result[source][symbol] = set()
            for target in targets:
                for key, group in reGroup.items():
                    if target in group:
                        result[source][symbol] = key
    return (result)

def deleteUselessState(Group, reGroup):
    """
    Reprend les classes formées précédemment et retire les états en doublon à condition que :
    -Les états viennent de la même classe
    -Les états ont les mêmes classes en cible

    Args:
         un dictionnaire avec des listes en valeurs, Un dictionnaire contenant un dictionnaire en valeur dans un set

    Returns:
        Deux dictionnaire contenant un dictionnaire en valeur dictionnaire ou chaine de caractère
    """
    result_dic = {}
    result_str = {}
    seen = []

    for source_2 in reGroup:
        for source, values in Group.items():
            if source in reGroup[source_2]:
                if values not in seen:
                    if source not in result_dic:
                        result_dic[source]=[]
                    result_dic[source].append(values)
                    result_str[source]= values
                    seen.append(values)
        seen = []

    return result_dic, result_str


def breakClass(Minimize, Group, reGroup):
    """
    Casse les classes qui ont des états qui ne peuvent pas être regroupés

    Args:
         Un dictionnaire contenant un dictionnaire en valeur dans un set, un dictionnaire avec des listes en valeurs

    Returns:
        Un dictionnaire contenant un dictionnaire en valeur dans un set
    """
    N_reGroup = {}

    for source, values in Minimize.items():
        for source2, values2 in Group.items():
            for source3, values3 in reGroup.items():
                if values2 == values and source2 in values3 and source in values3:
                    if str(source) not in N_reGroup:
                        N_reGroup[str(source)] = []
                    N_reGroup[str(source)].append(source2)

    return N_reGroup


def reCreateAutomaton(automaton, Minimize):
    """
    Transforme notre résultat qui a la forme d'un dictionnaire en automate de notre classe

    Args:
         Un automate, Un dictionnaire contenant un dictionnaire en valeur dans un set

    Returns:
        Notre automate final minimizé
    """
    New_automaton = Automaton(automaton.name)
    for source, values in Minimize.items():
        for mini in values:
            for symbol, targets in mini.items():
                    New_automaton.add_transition(source, symbol, targets)
                    if source in automaton.initial_states:
                        New_automaton.add_initial_state(source)
                    if source in automaton.final_states:
                        New_automaton.add_final_state(source)

    return New_automaton

def Minimization(automaton):
    """
   Fonction de minimisation avec toutes les fonctions étape par étape

    Args:
         Un automate

    Returns:
        L'automate minimisé
    """

    if not is_determinist(automaton):
        raise ValueError(f"L'automate {automaton.name} n'est pas déterministe")
    if not is_complete(automaton):
        raise ValueError(f"L'automate {automaton.name} n'est pas complet")

    Group_NT, Group_T = separationTerminal(automaton)
    Group_NT = regroup(automaton, Group_NT)
    Group_T = regroup(automaton, Group_T)
    reGroup = assemble(Group_NT, Group_T)
    Group = classification(automaton, reGroup)
    Minimize_dic, Minimize_str = deleteUselessState(Group, reGroup)

    while len(Minimize_dic) != len(reGroup):
        reGroup = breakClass(Minimize_str, Group, reGroup)
        Group = classification(automaton, reGroup)
        Minimize_dic, Minimize_str = deleteUselessState(Group, reGroup)
    result = reCreateAutomaton(automaton, Minimize_dic)

    if result == automaton:
        print(" ")
        print("L'automate est déja minimisé")
    return result

if __name__ == "__main__":
    from automaton.file_manager import read_automaton_from_file
    automaton = read_automaton_from_file("C:/Users/matte/dev/finite-automata-toolkit/automata_files/a44.txt")
    print(automaton)
    min_automaton = Minimization(automaton)
    print(min_automaton)