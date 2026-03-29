from .utils import *

class MenuOption:
    """Représente une option de menu avec un libellé et une action associée."""
    def __init__(self, label, action):
        """
        Args:
            label : le texte affiché pour cette option.
            action : la fonction appelée lorsque l'option est choisie.
        """
        self.label = label
        self.action = action

class Menu:
    """Représente un menu interactif en ligne de commande."""
    def __init__(self, title, options, allow_quit=True):
        """
        Args:
            title : le titre affiché en en-tête du menu.
            options : un dictionnaire associant une touche à une MenuOption.
            allow_quit : si True, l'utilisateur peut quitter avec "Q".
        """
        self.title = title
        self.options = options
        self.allow_quit = allow_quit

    def run(self):
        """
        Lance la boucle d'interaction du menu.

        Returns:
            Le résultat de l'action choisie, ou None si l'utilisateur quitte.
        """
        while True:
            self.display()
            choice = input("Votre choix : ").strip().lower()

            if self.allow_quit and choice == "q":
                print("")
                return None

            option = self.options.get(choice)
            if not option:
                print("Choix invalide.\n")
                continue

            try:
                print("")
                return option.action()
            except InputCancelled:
                print("Action annulée.\n")
                continue
            except Exception as e:
                print(f"Erreur : {e}\n")

    def display(self):
        """Affiche le titre et les options du menu dans la console."""
        display_header(self.title)
        for key, opt in self.options.items():
            print(f"{key}. {opt.label}")
        if self.allow_quit:
            print("Q. Quitter")
        print()