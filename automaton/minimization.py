# Mathias
from automaton import *

def separationTerminal(self):
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

    print(Group_NT)
    print(Group_T)
    return Group_NT, Group_T


def newGroup_NT(self, Group_NT):
    verif = []
    seen = []
    verif_unique = []
    rm = []
    i = 0
    for source in Group_NT:
        if len(Group_NT) == 1:
            verif.append(Group_NT[source])
            print(verif)
            return verif
        else:
            verif.append(Group_NT[source])
            i += 1

    for i in verif:
        if i not in seen:
            verif_unique.append(i)
            seen.append(i)

    print(verif_unique)
    return verif_unique

def Minimization(self):
    separationTerminal(self)




