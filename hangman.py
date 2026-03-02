import random

words = ["energy","motion","force","atom","light"]
secret = random.choice(words)
progress = ["_"] * len(secret)

mistakes = 0
limit = 6

print("Welcome to Hangman Game!")

while mistakes < limit and "_" in progress:
    print("word:", " ".join(progress))
    guess = input("Enter a letter: ").lower()

    if guess in secret:
        for i in range(len(secret)):
            if secret[i] == guess:
                progress[i] = guess
        print("Correct!\n")
    else:
        mistakes += 1
        print("Wrong! Attempts left:", limit - mistakes, "\n")


if "_" not in progress:
    print("You won! The word was:", secret)
else:
    print("Game is over! The word was:", secret)