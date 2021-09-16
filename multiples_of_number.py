def multiples_of_number(number):

    i = 0
    for num in range(1, number+1):
        if num % 3 == 0:
            print(num)
        elif num % 5 == 0:
            print(num)

multiples_of_number(17)
