# Mathias
from automaton import *

def minimisation(self):
    Group = {}
    for source, transitions in self.transitions.items():
        for symbol, targets in transitions.items():
            if source not in Group:
                Group[source] = {}
            if symbol not in Group[source]:
                Group[source][symbol] = set()
            for target in targets:
                if target not in self.final_states:
                    Group[source][symbol].add("NT")
                else :
                    Group[source][symbol].add("T")

    print(Group)




