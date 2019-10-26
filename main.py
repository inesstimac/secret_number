secret = 22

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess != secret:
        print("Sorry, your guess is not correct. Try again.")

    else:
        print("You guessed correctly, congratulations!")
        break
