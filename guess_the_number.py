def guess_the_number():

    import random
    list = []
    tries = 3
    number = int(random.randint(0, 10))
    print(number)
    while tries != 0:
        print(f'You have {tries} chances left. \nTry to guess \
any number between 0 through 10.')
        guess = int(input('What is the number? '))

        if number == guess:
            print('JACKPOT!!')
            break
        elif guess in list:
            continue
        else:
            if number < guess:
                print('Ouu that\'s high...')
            elif number > guess:
                print('Ouu that\'s low...')
        tries -= 1
        list.append(guess)

    while tries == 0:
        print('Sorry. Better luck next time.')
        break

guess_the_number()
