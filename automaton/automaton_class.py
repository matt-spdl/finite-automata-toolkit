import copy

AUTOMATON_DEFAULT_NAME = "Automate X"

class OrderedSet:
    def __init__(self):
        self._items = []

    def add(self, item):
        if item not in self._items:
            self._items.append(item)
            self._sort()

    def remove(self, item):
        self._items.remove(item)

    def discard(self, item):
        if item in self._items:
            self._items.remove(item)

    def clear(self):
        self._items.clear()

    def _sort(self):
        try:
            self._items.sort(key=lambda x: int(x))
        except ValueError:
            self._items.sort()

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return ", ".join(self._items)

    def __getitem__(self, index):
        return self._items[index]

class Automaton:
    """
    A class representing a finite automaton, which consists of states, an alphabet, transitions,
    and designated initial and final states.
    """

    def __init__(self, name = AUTOMATON_DEFAULT_NAME):
        """
        Initializes an empty automaton with:
        - A set of states.
        - A set of alphabet symbols.
        - An empty set of final states.
        - A dictionary for transitions.
        """
        self.name = name
        self.states = OrderedSet()
        self.alphabet = OrderedSet()
        self.initial_states = OrderedSet()
        self.final_states = OrderedSet()
        self.transitions = dict()

    def add_state(self, state):
        """
        Adds a state to the automaton.

        Args:
            state: The state to be added.
        """
        self.states.add(state)

        # Initialize the transition dictionary for the new state if it doesn't exist
        if state not in self.transitions:
            self.transitions[state] = dict()

    def add_initial_state(self, state):
        """
        Adds an initial state to the automaton.

        Args:
            state: The state to be added as an initial state.
        """
        self.add_state(state)
        self.initial_states.add(state)

    def add_final_state(self, state):
        """
        Adds a final state to the automaton.

        Args:
            state: The state to be added as a final state.
        """
        self.add_state(state)
        self.final_states.add(state)

    def add_transition(self, source, symbol, target):
        """
        Adds a transition to the automaton.

        Args:
            source: The source state of the transition.
            symbol: The symbol triggering the transition.
            target: The target state of the transition.
        """
        self.add_state(target)
        self.add_state(source)
        self.alphabet.add(symbol)

        # Create the transition if it doesn't exist
        if symbol not in self.transitions[source]:
            self.transitions[source][symbol] = OrderedSet()

        self.transitions[source][symbol].add(target)

    def is_final_state(self, state):
        return state in self.final_states

    def is_initial_state(self, state):
        return state in self.initial_states

    def get_target_states(self, state, symbol):
        """
        Retrieves the set of target states for a given state and symbol.

        Args:
            state: The current state.
            symbol: The symbol triggering the transition.

        Returns:
            A set of target states. Returns an empty set if no transition exists.
        """
        if state in self.transitions and symbol in self.transitions[state]:
            return self.transitions[state][symbol]
        return OrderedSet()

    def get_transitions_from_state(self, state):
        """
        Retrieves all transitions for a given state.

        Args:
            state: The state whose transitions are to be retrieved.

        Returns:
            A dictionary of transitions for the given state. Returns an empty dictionary if the state has no transitions.
        """
        if state in self.transitions:
            return self.transitions[state]
        return dict()

    def copy(self):
        """Creates a deep copy of the automaton."""
        new_automaton = Automaton(self.name)
        new_automaton.states = copy.deepcopy(self.states)
        new_automaton.alphabet = copy.deepcopy(self.alphabet)
        new_automaton.initial_states = copy.deepcopy(self.initial_states)
        new_automaton.final_states = copy.deepcopy(self.final_states)
        new_automaton.transitions = copy.deepcopy(self.transitions)

        return new_automaton

    def __repr__(self):
        string = [
            f"Nom : {self.name}",
            f"États : {self.states}",
            f"Alphabet : {self.alphabet}",
            f"États initiaux : {self.initial_states}",
            f"États finaux : {self.final_states}",
            "Transitions :"
        ]

        for source in self.transitions:
            for symbol in self.transitions[source]:
                targets = self.transitions[source][symbol]
                for target in targets:
                    string.append(f"  {source} --{symbol}--> {target}")

        return "\n".join(string)

if __name__ == "__main__":
    # Tests simples

    # 1) Construction
    a = Automaton()
    assert a.name == AUTOMATON_DEFAULT_NAME
    assert len(a.states) == 0
    assert len(a.alphabet) == 0
    assert len(a.initial_states) == 0
    assert len(a.final_states) == 0
    assert len(a.transitions) == 0

    # 2) add_state
    a.add_state("q0")
    assert "q0" in a.states
    assert "q0" in a.transitions  # transitions initialisées

    # 3) add_initial_state / add_final_state
    a.add_initial_state("q0")
    a.add_final_state("q1")
    assert a.is_initial_state("q0") is True
    assert a.is_initial_state("q1") is False
    assert a.is_final_state("q1") is True
    assert a.is_final_state("q0") is False
    assert "q1" in a.states  # add_final_state doit ajouter l'état

    # 4) add_transition
    a.add_transition("q0", "a", "q1")
    a.add_transition("q0", "b", "q2")
    assert "a" in a.alphabet
    assert "b" in a.alphabet
    assert "q2" in a.states

    # 5) get_target_states
    t_a = a.get_target_states("q0", "a")
    assert "q1" in t_a
    t_missing = a.get_target_states("q0", "c")
    assert len(t_missing) == 0

    # 6) get_transitions_from_state
    tr_q0 = a.get_transitions_from_state("q0")
    assert "a" in tr_q0
    assert "b" in tr_q0
    tr_missing_state = a.get_transitions_from_state("does_not_exist")
    assert len(tr_missing_state) == 0

    # 7) Unicité OrderedSet (états, alphabet, etc)
    a.add_state("q0")
    assert len([s for s in a.states if s == "q0"]) == 1
    a.alphabet.add("a")
    assert len([sym for sym in a.alphabet if sym == "a"]) == 1

    # 8) copy
    b = a.copy()
    assert b is not a
    assert b.name == a.name
    assert list(b.states) == list(a.states)
    assert list(b.alphabet) == list(a.alphabet)
    assert list(b.initial_states) == list(a.initial_states)
    assert list(b.final_states) == list(a.final_states)
    assert b.transitions is not a.transitions

    # modifier la copie ne doit pas modifier l'original
    b.add_state("q_copy_only")
    assert "q_copy_only" in b.states
    assert "q_copy_only" not in a.states

    print("Tous les tests simples ont réussi.")