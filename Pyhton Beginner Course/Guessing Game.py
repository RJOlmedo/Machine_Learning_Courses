secret_word = "Pancho"
word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        word = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Nah fam...")
else:
    print("That is right")