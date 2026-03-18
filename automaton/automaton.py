class Automaton:
    """
    A class representing a finite automaton, which consists of states, an alphabet, transitions,
    and designated initial and final states.
    """

    def __init__(self):
        """
        Initializes an empty automaton with:
        - A set of states.
        - A set of alphabet symbols.
        - An empty set of final states.
        - A dictionary for transitions.
        """
        self.states = set()
        self.alphabet = set()
        self.initial_states = set()
        self.final_states = set()
        self.transitions = {}

    def add_state(self, state):
        """
        Adds a state to the automaton.

        Args:
            state: The state to be added.
        """
        self.states.add(state)

        # Initialize the transition dictionary for the new state if it doesn't exist
        if state not in self.transitions:
            self.transitions[state] = {}

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
            self.transitions[source][symbol] = set()

        self.transitions[source][symbol].add(target)

    def get_next_states(self, state, symbol):
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
        return set()

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
        return {}

    def __str__(self):
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Initial state: {self.initial_states}")
        print(f"Final states: {self.final_states}")
        print("Transitions:")

        for state in self.transitions:
            for symbol in self.transitions[state]:
                targets = self.transitions[state][symbol]
                for target in targets:
                    print(f"  {state} -{symbol}-> {target}")
        return ""



if __name__ == "__main__":
    a = Automaton()
    a.add_initial_state("1")
    a.add_final_state("2")
    a.add_state("3")
    a.add_transition("1", "a", "2")
    a.add_transition("2", "a", "1")
    print(a.get_transitions_from_state("1"))
    print(a.get_next_states("1", "a"))
    print(a)

