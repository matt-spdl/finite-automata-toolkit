#Bastien
from automaton.automaton import Automaton

def recognition(automaton,word,indice,state):
    if indice == len(word) and state in automaton.final_states:
        return True
    if ((indice!=len(word) and word[indice] not in automaton.transitions[state] )
            or state=="P" or (indice==len(word) and state not in automaton.final_states)) :
        return False
    else:
        for i in automaton.get_target_states(state,word[indice]):
            if recognition(automaton,word,indice+1,i):
                return True
        return False

def word_recognition (automaton, word):
    for i in word:
        if i not in automaton.alphabet:
            return False
    for i in automaton.initial_states :
        if recognition(automaton,word,0,i):
            return True
    return False

def lire_mot (automaton) :
    mot_fin="fin"
    mot="nieheheh"
    while mot!= mot_fin:
        mot = input("Entrez le mot que vous voulez vérifier. Si vous voulez vous arrêter, entrez le mot 'fin'.")
        if word_recognition(automaton,mot):
            print("le mot "+mot+" est reconnu par l'automate")
        else:
            print("le mot " + mot + " n'est pas reconnu par l'automate")
    if mot==mot_fin:
        return True
    return False