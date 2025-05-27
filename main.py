import random, sys
words = ["tiger", "tree", "underground", "giraffe", "chair"]

remaining_attempts = 5
guessed_letters = ""

def select_word(words):
    return random.choice(words)

def print_hidden(hidden):
    for c in secret_word:
        if c in guessed_letters:
            print(" {} ".format(c), end = "")
        else:
            print(" _ ", end = "")
    print("\n")

def check_letter(guess):
    if len(guess) > 1 or not guess.isalpha():
        print("Invalid input!")
        return True
    if guess in guessed_letters:
        print("Invalid input!")
        return True
    if guess not in secret_word:
        print("wrong")
        return False
    return True

def check_win(word):
    for c in word:
        if c not in guessed_letters:
            return False
    return True

secret_word = select_word(words)
print(secret_word)

while remaining_attempts > 0:
    print_hidden(secret_word)
    print(guessed_letters)
    print(remaining_attempts)
    guess = input("Type a letter: ")
    while not check_letter(guess):
        remaining_attempts -= 1
        if remaining_attempts == 0:
            break
        print(remaining_attempts)
        guess = input("Type a letter: ")
    guessed_letters += guess

    if check_win(secret_word):
        print("WIN!!")
        sys.exit()

print("LOSE!!")
sys.exit()


