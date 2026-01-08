import random

words = ["python", "php", "html", "css", "django"]
notebook = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display_word = ""
    for letter in notebook:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "

    print("Word:", display_word)

    guess = input(" guess one letter : ").lower()

    if guess in guessed_letters:
        print("alredy guess your letter")
    elif guess in notebook:
        guessed_letters.append(guess)
        print("correct guess ")
    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("wrong guess ")
        print("Remaining chances:", max_wrong - wrong_guesses)

    if "_" not in display_word:
        print("🎉 Congratulations you win ")
        break

if wrong_guesses == max_wrong:
    print(" Game Over!")
    print("Correct word is:", notebook)
