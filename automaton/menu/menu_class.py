from input_utils import *

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
                return None

            option = self.options.get(choice)
            if not option:
                print("Choix invalide.\n")
                continue

            try:
                return option.action()
            except InputCancelled:
                print("Action annulée.\n")
                return None
            except Exception as e:
                print(f"Erreur : {e}\n")

    def _display_header(self):
        padding = 5
        padded_message = " " * padding + self.title + " " * padding
        length = len(padded_message)

        print("╔" + "═" * length + "╗")
        print("║" + padded_message + "║")
        print("╚" + "═" * length + "╝")

    def display(self):
        self._display_header()
        for key, opt in self.options.items():
            print(f"{key}. {opt.label}")
        if self.allow_quit:
            print("Q. Quitter")
        print()