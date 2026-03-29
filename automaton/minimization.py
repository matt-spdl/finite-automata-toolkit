# Mathias

from automaton import Automaton

def separationTerminal(self):
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
    for source, transitions in self.transitions.items():
        for symbol, targets in transitions.items():
            if source not in self.final_states:
                if source not in Group_NT:
                    Group_NT[source] = {}
                if symbol not in Group_NT[source]:
                    Group_NT[source][symbol] = set()
                for target in targets:
                    if target not in self.final_states:
                        Group_NT[source][symbol].add("NT")
                    else :
                        Group_NT[source][symbol].add("T")
            else :
                if source not in Group_T:
                    Group_T[source] = {}
                if symbol not in Group_T[source]:
                    Group_T[source][symbol] = set()
                for target in targets:
                    if target not in self.final_states:
                        Group_T[source][symbol].add("NT")
                    else:
                        Group_T[source][symbol].add("T")
    return Group_NT, Group_T


def regroup(self, Group):
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
            Assemble les deux dicctionnaires de listes des états terminaux et des états non-terminaux.

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

    print(result)
    return result

def classification(self, reGroup):
    """
            La fonction crée des classes (groupes) avec les groupes précédents formées
            et regroupe  dans un dictionnaire, tous les états de l'automates avec la classe de leur cible

            Args:
                Un dictionnaire, un dictionnaire avec des listes en valeurs

            Returns:
                Un dictionnaire contenant un dictionnaire en valeur dans un set
    """
    result = {}
    for source, transitions in self.transitions.items():
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
            Reprend les classes formés précdemment et retire les états en doublon à condition que :
            -Les états viennent de la même classe
            -Les étas ont les mêmes classes en cible

            Args:
                 un dictionnaire avec des listes en valeurs, Un dictionnaire contenant un dictionnaire en valeur dans un set

            Returns:
                Un dictionnaire contenant un dictionnaire en valeur dans un set
    """
    result = {}
    seen = []

    for source_2 in reGroup:
        for source, values in Group.items():
            if source in reGroup[source_2]:
                if values not in seen:
                    if source not in result:
                        result[source] = []
                    result[source].append(values)
                    seen.append(values)
        seen = []

    print(result)
    return result


def breakClass(Minimize, Regroup):
    """
            Casse les classes qui ont des états qui ne peuvent pas être regroupés

            Args:
                 Un dictionnaire contenant un dictionnaire en valeur dans un set, un dictionnaire avec des listes en valeurs

            Returns:
                Un dictionnaire contenant un dictionnaire en valeur dans un set
    """
    N_reGroup = {}
    j=0
    prev = []

    for source, values in Minimize.items():
        prev.append(source)

    for source,values in Minimize.items():
        for source2,values2 in Regroup.items():
            if source in values2:
                for i in range(len(prev)):
                    if str(i) in values2:
                        j += 1

                if j > 1:
                    N_reGroup[str(source)] = []
                    N_reGroup[str(source)].append(source)
                else :
                    N_reGroup[str(source)] = values2
                j = 0


    print(N_reGroup)
    return N_reGroup


def reCreateAutomaton(self, Minimize):
    """
            Transforme notre résultat qui a la forme d'un dictionnaire en automate de notre classe

            Args:
                 Un automate, Un dictionnaire contenant un dictionnaire en valeur dans un set

            Returns:
                Notre automate final minimizé
    """
    New_automaton = Automaton()
    for source, values in Minimize.items():
        for mini in values:
            for symbol, targets in mini.items():
                for target in targets:
                    New_automaton.add_transition(source, symbol, target)
                    if source in self.initial_states:
                        New_automaton.add_initial_state(source)
                    if source in self.final_states:
                        New_automaton.add_final_state(source)

    return New_automaton

def Minimization(self):
    """
           Fonction de minimisation avec toues les fonctions étape par étape

            Args:
                 Un automate

            Returns:
                L'automate minimisé
    """
    Group_NT, Group_T = separationTerminal(self)
    Group_NT = regroup(self, Group_NT)
    Group_T = regroup(self, Group_T)
    reGroup = assemble(Group_NT, Group_T)
    Group = classification(self, reGroup)
    Minimize = deleteUselessState(Group, reGroup)
    while len(Minimize) != len(reGroup):
        reGroup = breakClass(Minimize, reGroup)
        Group = classification(self, reGroup)
        Minimize = deleteUselessState(Group, reGroup)
    result = reCreateAutomaton(self, Minimize)
    print(result)
    return result


