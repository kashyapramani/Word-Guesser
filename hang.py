import random


def get_input():
    while True:
        min_length = input("Enter the length of the word between 4-10 :  ").strip()
        if min_length.isnumeric():
            break

    while True:
        n = input("Enter the number of incorrect attempts between 1 and 25:  ").strip()
        if n.isnumeric() and int(n) in range(1, 26):
            break

    return int(min_length), int(n)


def get_word(length):
    with open("words.txt", "r") as f:
        print("Selecting a Word.........\n")
        data = f.readlines()

        while True:
            word = random.choice(data).strip()

            if len(word) == length:
                break

        return word


def check_word():
    positions = []
    while True:
        c = input("Choose a Letter: ")
        if c not in GUESSED:
            break
        print("' {} ' is already guessed. Try something new...!!".format(c))

    GUESSED.add(c)
    start = 0

    while True:
        index = WORD.find(c, start)
        if index != -1:
            positions.append(index)
            start = index + 1
        else:
            break

    if len(positions) == 0:
        print("' {} ' is not in the Word. ".format(c))
        return 0

    print("' {} ' is in the Word !".format(c))
    for i in positions:
        STRING[i] = c

    return len(positions)


def string():
    return ' '.join(c for c in STRING)


if __name__ == "__main__":

    print("Welcome to the word of HANGMAN")

    word_length, attempts = get_input()
    WORD = get_word(word_length)
    STRING = ["_"] * word_length
    global GUESSED
    GUESSED = {""}
    remaining = word_length

    while attempts > 0 and remaining > 0:
        print("\nWord: ", string())
        print("attempts Remaining:  ", attempts)
        # print("Guessed Letters: ", GUESSED)

        k = check_word()
        if k == 0:
            attempts -= 1
        else:
            remaining -= k

    print("\nWord:  ", WORD)

    if attempts == 0 or remaining != 0:
        print("\nYou couldn't save a life....\nBetter Luck Next Time...!!")
    else:
        print("\n\nWell Played......!!!!!!!")
        print("Bye Bye \n\n")
