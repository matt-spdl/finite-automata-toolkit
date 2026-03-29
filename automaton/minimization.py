# Mathias

from automaton import Automaton

def separationTerminal(self):
    """
            Splits the automaton states into two dictionaries:
            terminal states and non-terminal states,
            then replaces their targets with "T" or "NT" depending on whether the target is terminal or not.

            Args:
                an automaton

            Returns:
                two dictionaries of dictionaries
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
            Groups states that have similar targets into new groups.

            Args:
                an automaton, a dictionary of dictionaries

            Returns:
                a dictionary containing lists
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
            Merges two dictionaries into a single one.

            Args:
                two dictionaries containing lists

            Returns:
                a dictionary containing lists
            """
    result ={}
    i = 1

    for values in Group_NT.values():
        result[str(i)] = values
        i += 1

    for values in Group_T.values():
        result[str(i)] = values
        i += 1

    print(result)
    return result

def classification(self, reGroup):
    """
            Creates a dictionary of dictionaries by replacing states
            with the new groups formed by the previous functions.

            Args:
                an automaton, a dictionary of lists

            Returns:
                a dictionary containing dictionaries
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
            Removes duplicate states that belong to the same groups
            in the new classification.

            Args:
                 a dictionary of lists, a dictionary of dictionaries

            Returns:
                a dictionary containing lists of dictionaries
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

    return result

'''
def newRegroup(Minimize, Regroup):
    N_reGroup = {}
    i=0

    for source,values in Regroup.items():
        for source2,values2 in Minimize.items():
            for j in range(len(values)):
                if values[j] == source2:
                    i+=1
        if i > 1:
            N_reGroup[str(source)] = source
        else :
            N_reGroup[str(source)] = values
        i = 0

    print(N_reGroup)
    return N_reGroup
'''

def reCreateAutomaton(self, Minimize):
    """
            Transforms the dictionary into a new automaton.

            Args:
                 an automaton, a dictionary of lists of dictionaries

            Returns:
                the new automaton built from the dictionary
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
            Minimizes an automaton by applying all the steps.

            Args:
                 an automaton

            Returns:
                the minimized automaton
            """
    Group_NT, Group_T = separationTerminal(self)
    Group_NT = regroup(self, Group_NT)
    Group_T = regroup(self, Group_T)
    reGroup = assemble(Group_NT, Group_T)
    Group = classification(self, reGroup)
    Minimize = deleteUselessState(Group, reGroup)
    '''
    while len(Minimize) != len(reGroup):
        reGroup = newRegroup(Minimize, reGroup)
        Group = classification(self, reGroup)
        Minimize = deleteUselessState(Group, reGroup)
    '''
    result = reCreateAutomaton(self, Minimize)
    print(result)
    return result


A = Automaton()

# États
A.add_state("0")
A.add_state("1")
A.add_state("2")
A.add_state("3")
A.add_state("4")
A.add_state("5")

# État initial
A.add_initial_state("0")

# États finaux
A.add_final_state("3")
A.add_final_state("4")
A.add_final_state("5")

# Transitions
A.add_transition("0", "a", "1")
A.add_transition("0", "b", "0")

A.add_transition("1", "a", "1")
A.add_transition("1", "b", "2")

A.add_transition("2", "a", "3")
A.add_transition("2", "b", "0")

# Une fois "aba" trouvé → on reste dans un état final
A.add_transition("3", "a", "4")
A.add_transition("3", "b", "5")

A.add_transition("4", "a", "4")
A.add_transition("4", "b", "5")

A.add_transition("5", "a", "4")
A.add_transition("5", "b", "5")

print(A)
Minimization(A)


