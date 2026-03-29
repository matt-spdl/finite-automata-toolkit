from automaton import is_determinist
from automaton.determinization import determinize
from automaton.display import *
from automaton.minimization import *
from automaton.completion import *
from automaton.standardization import *

def write_automatons(file):
    """
    Affiche l'automate initial, sa version déterministe (si nécessaire),
    puis sa version minimisée et complète.

    Args:
        file : le chemin vers le fichier de l'automate.
    """
    #récupération de l'automate
    new_automaton=read_automaton_from_file(file)

    #affichage de l'automate sans changement
    print("automate initial:")
    print("")
    display_automaton_table(new_automaton)

    #affichage de l'automate standardisé si besoin
    if not is_standard(new_automaton):
        print("")
        print("automate standardisé:")
        print("")
        display_automaton_table(standardization(new_automaton))
    else:
        print("")
        print("l'automate est déjà standard")

    #affichage de l'automate déterministe si besoin
    if not is_determinist(new_automaton):
        determinize_automaton=determinize(new_automaton)
        print("")
        print("automate déterministe:")
        print("")
        display_automaton_table(determinize_automaton)
    else:
        determinize_automaton=new_automaton
        print("")
        print("l'automate est déjà déterministe")

    #affichage de l'automate minimisé et complet si besoin
    if is_complete(determinize_automaton):
        minimized_automaton = Minimization(determinize_automaton)
    else:
        minimized_automaton = Minimization(completion(determinize_automaton))
    print("")
    print("automate minimisé et complet:")
    print("")
    display_automaton_table(minimized_automaton)
    print("")

def choose_automaton():
    """Parcourt tous les automates (1 à 44) et affiche leurs informations."""
    choice=1
    while choice<45:
        match choice:
            case 1:
                print("")
                print("informations de l'automate 1:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a1.txt")
            case 2:
                print("")
                print("informations de l'automate 2:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a2.txt")
            case 3:
                print("")
                print("informations de l'automate 3:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a3.txt")
            case 4:
                print("")
                print("informations de l'automate 4:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a4.txt")
            case 5:
                print("")
                print("informations de l'automate 5:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a5.txt")
            case 6:
                print("")
                print("informations de l'automate 6:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a6.txt")
            case 7:
                print("")
                print("informations de l'automate 7:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a7.txt")
            case 8:
                print("")
                print("informations de l'automate 8:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a8.txt")
            case 9:
                print("")
                print("informations de l'automate 9:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a9.txt")
            case 10:
                print("")
                print("informations de l'automate 10:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a10.txt")
            case 11:
                print("")
                print("informations de l'automate 11:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a11.txt")
            case 12:
                print("")
                print("informations de l'automate 12:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a12.txt")
            case 13:
                print("")
                print("informations de l'automate 13:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a13.txt")
            case 14:
                print("")
                print("informations de l'automate 14:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a14.txt")
            case 15:
                print("")
                print("informations de l'automate 15:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a15.txt")
            case 16:
                print("")
                print("informations de l'automate 16:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a16.txt")
            case 17:
                print("")
                print("informations de l'automate 17:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a17.txt")
            case 18:
                print("")
                print("informations de l'automate 18:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a18.txt")
            case 19:
                print("")
                print("informations de l'automate 19:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a19.txt")
            case 20:
                print("")
                print("informations de l'automate 20:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a20.txt")
            case 21:
                print("")
                print("informations de l'automate 21:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a21.txt")
            case 22:
                print("")
                print("informations de l'automate 22:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a22.txt")
            case 23:
                print("")
                print("informations de l'automate 23:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a23.txt")
            case 24:
                print("")
                print("informations de l'automate 24:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a24.txt")
            case 25:
                print("")
                print("informations de l'automate 25:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a25.txt")
            case 26:
                print("")
                print("informations de l'automate 26:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a26.txt")
            case 27:
                print("")
                print("informations de l'automate 27:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a27.txt")
            case 28:
                print("")
                print("informations de l'automate 28:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a28.txt")
            case 29:
                print("")
                print("informations de l'automate 29:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a29.txt")
            case 30:
                print("")
                print("informations de l'automate 30:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a30.txt")
            case 31:
                print("")
                print("informations de l'automate 31:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a31.txt")
            case 32:
                print("")
                print("informations de l'automate 32:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a32.txt")
            case 33:
                print("")
                print("informations de l'automate 33:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a33.txt")
            case 34:
                print("")
                print("informations de l'automate 34:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a34.txt")
            case 35:
                print("")
                print("informations de l'automate 35:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a35.txt")
            case 36:
                print("")
                print("informations de l'automate 36:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a36.txt")
            case 37:
                print("")
                print("informations de l'automate 37:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a37.txt")
            case 38:
                print("")
                print("informations de l'automate 38:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a38.txt")
            case 39:
                print("")
                print("informations de l'automate 39:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a39.txt")
            case 40:
                print("")
                print("informations de l'automate 40:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a40.txt")
            case 41:
                print("")
                print("informations de l'automate 41:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a41.txt")
            case 42:
                print("")
                print("informations de l'automate 42:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a42.txt")
            case 43:
                print("")
                print("informations de l'automate 43:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a43.txt")
            case 44:
                print("")
                print("informations de l'automate 44:")
                print("")
                write_automatons("C:/Users/BastienP/PycharmProjects/finite-automata-toolkit/automata_files/a44.txt")
        choice+=1


choose_automaton()