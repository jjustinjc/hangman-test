import random

# selects random word from wordlist.txt and returns it in full lowercase
def select_word():
    with open('wordlist.txt') as f:
        return str(random.choice(f.readlines())).lower()

# iterates through each letter in the selected word s
# and compares them with guessed letter list g
def print_hidden(s, g):
    for c in s:
        if c in g:
            print(" {} ".format(c), end = "")
        else:
            print(" _ ", end = "")
    print("\n")

# check whether the guess is a valid character, if it is already in g, or if it is wrong
def check_letter(guess, s, g):
    if len(guess) > 1 or not guess.isalpha():
        print("Invalid input!")
        return True
    if guess in g:
        print("Invalid input!")
        return True
    if guess not in s:
        print("wrong")
        return False
    return True

#check if each letter in secret word s matches
# with a character in guessed letter list g
def check_win(s, g):
    for c in s:
        if c not in g:
            return False
    return True