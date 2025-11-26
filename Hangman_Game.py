
import random
from words import WORDS
from art import display_man, HANGMAN_ART


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def run_game():
    answer = random.choice(WORDS).upper()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = len(HANGMAN_ART) - 1
    is_running = True

    while is_running:
        print("-" * 30)
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Geratene Buchstaben: {' '.join(sorted(guessed_letters))}")

        guess = input("Gib einen Buchstaben ein: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Bitte gib einen einzelnen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print(f"❗ {guess} wurde bereits geraten.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Falsch! Fehler: {wrong_guesses}/{max_wrong}")

        if "_" not in hint:
            print("-" * 30)
            display_man(wrong_guesses)
            display_answer(answer)
            print("🎉 GEWONNEN!")
            is_running = False
        elif wrong_guesses >= max_wrong:
            print("-" * 30)
            display_man(wrong_guesses)
            display_answer(answer)
            print("⚰️  VERLOREN!⚰️")
            is_running = False
