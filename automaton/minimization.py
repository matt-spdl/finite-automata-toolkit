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

'''
def newGroup(self, Group):
    verif = []
    i=0
    for source in Group:
        i += 1
        verif[i] = Group[source]
    for k in range(1, i+1):
        for j in range(1, i+1):
            if i != j:
                if verif[i]==verif[j]:
                
'''



def Minimization(self):
    separationTerminal(self)




