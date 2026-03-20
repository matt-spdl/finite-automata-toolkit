# Mathias

from automaton.automaton import Automaton

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
                        Group_T[source][symbol] = "NT"
                    else:
                        Group_T[source][symbol] = "T"

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
                    if source_2 not in result:
                        result[source_2] = []
                    result[source_2].append(values)
                    seen.append(values)
        seen = []

    return result

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
    result = reCreateAutomaton(self, Minimize)
    print(result)
    if result == self:
        print("Automaton was already minimized")
    return result

a = Automaton()
a.add_initial_state("1")
a.add_final_state("2")
a.add_state("3")
a.add_transition("1", "a", "2")
a.add_transition("1", "b", "3")
a.add_transition("2", "a", "4")
a.add_transition("2", "b", "2")
a.add_transition("3", "a", "2")
a.add_transition("3", "b", "1")
a.add_transition("4", "b", "2")
a.add_transition("4", "a", "4")
print(a)
Minimization(a)