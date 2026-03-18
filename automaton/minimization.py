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


def regroup(self, Group):
    result = {}
    compar = {}
    i = 1
    for source,values in Group.items():
        if len(Group) == 1:
            result[1]=source
            print(result)
            return result
        else:
            verif = str(values)
            if verif not in compar:
                compar[verif] = []
            compar[verif].append(source)

    for verif in compar.values():
        result[i]=verif
        i += 1

    print(result)
    return result

def Minimization(self):
    separationTerminal(self)




