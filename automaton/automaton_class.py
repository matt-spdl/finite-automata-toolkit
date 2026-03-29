import copy

AUTOMATON_DEFAULT_NAME = "Automate X"

class OrderedSet:
    """Ensemble ordonné qui maintient les éléments triés et sans doublons."""
    def __init__(self):
        """Initialise un ensemble ordonné vide."""
        self._items = []

    def add(self, item):
        """Ajoute un élément s'il n'est pas déjà présent, puis trie l'ensemble."""
        if item not in self._items:
            self._items.append(item)
            self._sort()

    def remove(self, item):
        """Supprime un élément de l'ensemble (lève ValueError s'il est absent)."""
        self._items.remove(item)

    def discard(self, item):
        """Supprime un élément s'il est présent, sans lever d'erreur sinon."""
        if item in self._items:
            self._items.remove(item)

    def clear(self):
        """Vide l'ensemble."""
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

    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            return NotImplemented
        return set(self._items) == set(other._items)

class Automaton:
    """
    Classe représentant un automate fini, composé d'états, d'un alphabet,
    de transitions, et d'états initiaux et finaux.
    """

    def __init__(self, name = AUTOMATON_DEFAULT_NAME):
        """
        Initialise un automate vide avec :
        - Un ensemble d'états.
        - Un alphabet.
        - Un ensemble d'états finaux vide.
        - Un dictionnaire de transitions vide.
        """
        self.name = name
        self.states = OrderedSet()
        self.alphabet = OrderedSet()
        self.initial_states = OrderedSet()
        self.final_states = OrderedSet()
        self.transitions = dict()

    def add_state(self, state):
        """
        Ajoute un état à l'automate.

        Args:
            state : l'état à ajouter.
        """
        self.states.add(state)

    def add_symbol(self, symbol):
        """
        Ajoute un symbole à l'alphabet de l'automate.

        Args:
            symbol : le symbole à ajouter.
        """
        self.alphabet.add(symbol)

    def add_initial_state(self, state):
        """
        Ajoute un état initial à l'automate.

        Args:
            state : l'état à définir comme état initial.
        """
        self.add_state(state)
        self.initial_states.add(state)

    def add_final_state(self, state):
        """
        Ajoute un état final à l'automate.

        Args:
            state : l'état à définir comme état final.
        """
        self.add_state(state)
        self.final_states.add(state)

    def add_transition(self, source, symbol, target):
        """
        Ajoute une transition à l'automate.

        Args:
            source : l'état source de la transition.
            symbol : le symbole déclenchant la transition.
            target : l'état cible de la transition.
        """
        self.add_state(target)
        self.add_state(source)
        self.alphabet.add(symbol)

        # Initialise le dictionnaire de transitions pour le nouvel état s'il n'existe pas
        if source not in self.transitions:
            self.transitions[source] = dict()

        # Crée la transition si elle n'existe pas encore
        if symbol not in self.transitions[source]:
            self.transitions[source][symbol] = OrderedSet()

        self.transitions[source][symbol].add(target)

    def is_final_state(self, state):
        """Retourne True si l'état donné est un état final."""
        return state in self.final_states

    def is_initial_state(self, state):
        """Retourne True si l'état donné est un état initial."""
        return state in self.initial_states

    def get_target_states(self, state, symbol):
        """
        Retourne l'ensemble des états cibles pour un état et un symbole donnés.

        Args:
            state : l'état courant.
            symbol : le symbole déclenchant la transition.

        Returns:
            Un ensemble d'états cibles. Retourne un ensemble vide si aucune transition n'existe.
        """
        if state in self.transitions and symbol in self.transitions[state]:
            return self.transitions[state][symbol]
        return OrderedSet()

    def get_transitions_from_state(self, state):
        """
        Retourne toutes les transitions d'un état donné.

        Args:
            state : l'état dont on veut récupérer les transitions.

        Returns:
            Un dictionnaire de transitions pour l'état donné.
            Retourne un dictionnaire vide si l'état n'a pas de transitions.
        """
        if state in self.transitions:
            return self.transitions[state]
        return dict()

    def copy(self):
        """Crée une copie profonde de l'automate."""
        new_automaton = Automaton(self.name)
        new_automaton.states = copy.deepcopy(self.states)
        new_automaton.alphabet = copy.deepcopy(self.alphabet)
        new_automaton.initial_states = copy.deepcopy(self.initial_states)
        new_automaton.final_states = copy.deepcopy(self.final_states)
        new_automaton.transitions = copy.deepcopy(self.transitions)

        return new_automaton

    def __repr__(self):
        """Retourne une représentation textuelle de l'automate."""
        string = [
            f"Nom : {self.name}",
            f"États : {self.states}",
            f"Alphabet : {self.alphabet}",
            f"États initiaux : {self.initial_states}",
            f"États finaux : {self.final_states}",
            "Transitions :"
        ]
        if len(self.transitions) == 0:
            string.append("  (Aucune transition)")
        else:
            for source in self.transitions:
                for symbol in self.transitions[source]:
                    targets = self.transitions[source][symbol]
                    for target in targets:
                        string.append(f"  {source} --{symbol}--> {target}")

        return "\n".join(string)

    def __eq__(self, other):
        """Vérifie l'égalité entre deux automates (états, alphabet, transitions identiques)."""
        if not isinstance(other, Automaton):
            return NotImplemented
        if self.states != other.states:
            return False
        if self.alphabet != other.alphabet:
            return False
        if self.initial_states != other.initial_states:
            return False
        if self.final_states != other.final_states:
            return False
        if self.transitions != other.transitions:
            return False
        return True


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

    # 9) __eq__
    c = a.copy()
    assert a == c
    c.add_transition("q0", "c", "q1")
    assert a != c

    print("Tous les tests simples ont réussi.")