from utils import *

class MenuOption:
    def __init__(self, label, action):
        self.label = label
        self.action = action

class Menu:
    def __init__(self, title, options, allow_quit=True):
        self.title = title
        self.options = options
        self.allow_quit = allow_quit

    def run(self):
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
        display_header(self.title)
        for key, opt in self.options.items():
            print(f"{key}. {opt.label}")
        if self.allow_quit:
            print("Q. Quitter")
        print()