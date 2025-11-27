

import random
import sys


WORDS_9 = [
    "pineapple",  # 9
    "algorithm",  # 9
    "developer",  # 9
    "beautiful",  # 9
    "formation",  # 9
    "framework",  # 9
    "togethern",  # 9 
]

MAX_MISSES = 9  

def choose_word(word_list):
    return random.choice(word_list).lower()

def display_state(word, guessed_letters):
    
    parts = []
    for c in word:
        if c in guessed_letters:
            
            parts.append("****" + c + "****")
        else:
            parts.append("_")
    
    return "".join(parts)

def get_guess(already_guessed):
    while True:
        guess = input("Ange en gissning (en bokstav eller hela ordet): ").strip().lower()
        if not guess:
            print("Skriv en bokstav eller ett ord.")
            continue
        if len(guess) == 1:
            if not guess.isalpha():
                print("Använd endast bokstäver.")
                continue
            if guess in already_guessed:
                print("Du har redan gissat den bokstaven.")
                continue
            return guess
        else:
            
            if not guess.isalpha():
                print("Använd endast bokstäver när du gissar hela ord.")
                continue
            return guess

def play_round():
    word = choose_word(WORDS_9)
    guessed_letters = set()
    wrong_guesses = []
    misses_left = MAX_MISSES

    
    print(f'\nDu ska gissa ett ord, bokstav för bokstav, på 9 bokstäver ange en gissing -> _ du har nu {misses_left} st felgissningar kvar. Felgissningar : ')

    while True:
        state = display_state(word, guessed_letters)
        print("\nOrd: ", state)
        print(f"Du har nu {misses_left} st felgissningar kvar.")
        print("Felgissningar :", " ".join(wrong_guesses) if wrong_guesses else "(inga)")

        guess = get_guess(guessed_letters.union(set(wrong_guesses)))

        if len(guess) > 1:
            
            if guess == word:
                
                guessed_letters.update(set(word))
                print("\nGrattis! Du gissade rätt ordet:", word)
                return True
            else:
                misses_left -= 1
                wrong_guesses.append(guess)
                print("Fel gissat hela ordet.")
        else:
           
            if guess in word:
                guessed_letters.add(guess)
                print(f"Rätt bokstav: '{guess}' är i ordet.")
               
                if all(c in guessed_letters for c in set(word)):
                    print("\nGrattis — du klarade det! Ordet var:", word)
                    return True
            else:
                misses_left -= 1
                wrong_guesses.append(guess)
                print(f"Fel bokstav: '{guess}'")

        if misses_left <= 0:
            print("\nDu har inga felgissningar kvar. Game over!")
            print("Rätt ord var:", word)
            return False

def main():
    print("=== Ordgissningsspel (9 bokstäver) ===")
    while True:
        play_round()
        again = input("\nSpela igen? (j/n): ").strip().lower()
        if again != "j":
            print("Tack för spelet! Hej då.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAvslutar. Hej!")
        sys.exit(0)



