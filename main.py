import sys
import hangman_functions as h
remaining_attempts = 5
guessed_letters = ""

secret_word = h.select_word()
print(secret_word)

while remaining_attempts > 0:
    h.print_hidden(secret_word, guessed_letters)
    print(guessed_letters)
    print(remaining_attempts)
    guess = input("Type a letter: ")

    while not h.check_letter(guess, secret_word, guessed_letters):
        remaining_attempts -= 1
        if remaining_attempts == 0:
            break
        print(remaining_attempts)
        guess = input("Type a letter: ")

    guessed_letters += guess

    if h.check_win(secret_word, guessed_letters):
        print("WIN!!")
        sys.exit()

print("LOSE!!")
sys.exit()


