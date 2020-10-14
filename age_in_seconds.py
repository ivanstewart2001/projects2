while True:
    user_age = int(input("How old are you?: "))

    calculation = user_age * 365 * 24 * 60 * 60
    
    message = "You are {} seconds old.".format(calculation)

    print(message)

    restart = input("Would you like to restart (y/n)?: ").strip().lower()
    if restart == "y":
        pass
    else:
        break