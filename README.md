# finite-automata-toolkit

## Contributeurs : 

- Louis LEMONNIER
- Mattéo SPINDLER
- Mathias LEROY
- Bastien POMMARD
- Thomas AUBERT

## Objectifs du projet :

L'objectif de ce projet est de réaliser un programme en python ou C pour réaliser des traitements automatiques sur des automates :
- Minimisation
- Standradisation
- Complétion
- Déterminisation
- Minimisation
- Reconnaissance de mots
Le projet demande également de réaliser un affichage des automates. 

## Organisation du projet 

- Dossier **automata_files** qui contient les différents automates à tester
- Dossier **automaton** qui contient tous les fichiers python pour réaliser les traitements sur les automates
- Dossier **cli** qui contient les fichiers python dédiés à l'affichage
- le fichier **main.py** qui contient la boucle pour lancer tout le projet

## Répartition des tâches

- Louis LEMONNIER s'occupe de Standardisation / Complémentation
- Mattéo SPINDLER réalise File Manager / Display
- Mathias LEROY code la Minimisation
- Bastien POMMARD fait Complétion / Properties
- Thomas AUBERT s'occupe de la Déterminisation


## ⚠️Comment lancer le projet ⚠️

Pour lancer le projet, il suffit d'exécuter le fichier **main.py** et de suivre les instructions du menu. Pour sélectionner l'automate à traiter, il suffit de soit taper le nom de l'automate, soit 
d'écrire le chemin absolu vers l'automate. 

Si on veut ajouter des automates qui ne font pas parti de ceux déjà présent dans le dossier, les automates doivent respecter OBLIGATOIREMENT la structure suivante : 

- Ligne 1 : nom de l'automate
- Ligne 2 : liste des symboles de l’alphabet séparés par des espaces.
- Ligne 3 : indices des états initiaux séparés par des espaces.
- Ligne 4 : indices des états finaux séparés par des espaces.
- Lignes 5 et suivantes : transitions sous la forme : état de départ <symbole> état d’arrivée











