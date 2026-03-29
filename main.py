from automaton import read_automaton_from_file, display_automaton_table

automaton = read_automaton_from_file("C:/Users/taube/Desktop/Cours EFREI/S4/Automates/finite-automata-toolkit-main/automata_files")
print(automaton)

display_automaton_table(automaton)