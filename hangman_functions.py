import random
def select_word():
    with open('wordlist.txt') as f:
        return str(random.choice(f.readlines())).lower()


def print_hidden(s, g):
    for c in s:
        if c in g:
            print(" {} ".format(c), end = "")
        else:
            print(" _ ", end = "")
    print("\n")

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

def check_win(word, g):
    for c in word:
        if c not in g:
            return False
    return True