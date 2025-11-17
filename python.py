import random

# Lista med ord att gissa
words = ["python", "skola", "dator", "program", "kodning", "spel"]

# Väljer ett slumpmässigt ord
word = random.choice(words)
hidden_word = ["_" for _ in word]

# Antal försök
tries = 10

def print_status():
    print("\nOrd: ", " ".join(hidden_word))
    print(f"Kvarvarande gissningar: {tries}")