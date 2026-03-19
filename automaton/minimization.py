# Mathias

import automaton

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

def assemble(Group_NT, Group_T):
    result ={}
    i = 1

    for values in Group_NT.values():
        result[str(i)] = values
        i += 1

    for values in Group_T.values():
        result[str(i)] = values
        i += 1

    return result

def classification(self, Group):
    result = {}
    for source, transitions in self.transitions.items():
        for symbol, targets in transitions.items():
            if source not in result:
                result[source] = {}
            if symbol not in result[source]:
                result[source][symbol] = set()
            for target in targets:
                for key, group in Group.items():
                    if target in group:
                        result[source][symbol].add(key)

    print(result)
    return (result)

def deleteUselessState(Group, reGroup):
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


def reCreateAutomaton(self, Minimize):
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
    Group_NT, Group_T = separationTerminal(self)
    Group_NT = regroup(self, Group_NT)
    Group_T = regroup(self, Group_T)
    reGroup = assemble(Group_NT, Group_T)
    Group = classification(self, reGroup)
    Minimize = deleteUselessState(Group, reGroup)
    result = reCreateAutomaton(self, Minimize)
    return result



