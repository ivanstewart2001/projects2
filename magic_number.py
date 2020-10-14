from random import randint

while True:
    magic_number = randint(1,10)

    user_guess = int(input("Guess a number 1-10: "))

    if magic_number == user_guess:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly.")

    restart = input("Would you like to guess again (y/n)?: ").strip().lower()
    if restart == "y":
        pass
    else:
        break

