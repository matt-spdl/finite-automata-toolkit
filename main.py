from automaton import read_automaton_from_file, display_automaton_table

automaton = read_automaton_from_file("C:/Users/matte/dev/finite-automata-toolkit/automata_files/automate.exemple.txt")
print(automaton)

display_automaton_table(automaton)