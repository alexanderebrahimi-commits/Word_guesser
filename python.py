import random

WORD_LIST = [
    "tillstånd",
    "maskering",
    "innehålls",
    "fördelen",
    "formation",
    "beautiful",
]

MAX_WRONG_GUESSES = 9

def choose_random_word(word_list):
    return random.choice(word_list).lower()

def format_word_state(secret_word, guessed_letters):
    formatted = []
    for letter in secret_word:
        if letter in guessed_letters:
            formatted.append(f"****{letter}****")
        else:
            formatted.append("_")
    return "".join(formatted)

def get_user_guess(previous_guesses):
    while True:
        guess = input("Ange en gissning (en bokstav eller hela ordet): ").strip().lower()
        if not guess:
            print("Du måste skriva något.")
            continue
        if not guess.isalpha():
            print("Endast bokstäver är tillåtna.")
            continue
        if guess in previous_guesses:
            print("Du har redan gissat detta.")
            continue
        return guess

def play_round():
    secret_word = choose_random_word(WORD_LIST)
    guessed_letters = set()
    wrong_guesses = []
    guesses_left = MAX_WRONG_GUESSES

    print(f"\nDu ska gissa ett ord på 9 bokstäver.")
    print(f"Du har {guesses_left} felgissningar.")
    print("Felgissningar: (inga ännu)")

    while True:
        print("\nOrdet:", format_word_state(secret_word, guessed_letters))
        print(f"Kvarvarande felgissningar: {guesses_left}")
        print("Felgissningar:", " ".join(wrong_guesses) if wrong_guesses else "(inga)")

        guess = get_user_guess(guessed_letters.union(wrong_guesses))

        if len(guess) == 1:
            if guess in secret_word:
                guessed_letters.add(guess)
                print(f"Rätt! Bokstaven '{guess}' finns i ordet.")
                if all(letter in guessed_letters for letter in set(secret_word)):
                    print("\nDu vann! Ordet var:", secret_word)
                    return True
            else:
                wrong_guesses.append(guess)
                guesses_left -= 1
                print("Fel bokstav.")
        else:
            if guess == secret_word:
                print("\nDu vann! Ordet var:", secret_word)
                return True
            else:
                wrong_guesses.append(guess)
                guesses_left -= 1
                print("Fel ord.")

        if guesses_left == 0:
            print("\nDu förlorade! Ordet var:", secret_word)
            return False

def main():
    print("=== Word Guesser – 9 bokstäver ===")
    while True:
        play_round()
        again = input("\nVill du spela igen? (j/n): ").strip().lower()
        if again != "j":
            print("Hejdå!")
            break

if __name__ == "__main__":
    main()

