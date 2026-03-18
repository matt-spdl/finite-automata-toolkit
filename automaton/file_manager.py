from automaton.automaton import Automaton
from pathlib import Path

def read_automaton(filename) -> Automaton :
    path = Path(filename)
    print(f"Path : {path}")

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {filename}")

    if path.suffix != ".txt":
        raise ValueError(f"Invalid file format: {filename}. Expected a .txt file.")

    with path.open() as file:
        print(file.read())

    return Automaton()