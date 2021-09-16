def multiplication_table(n):

    for number in range(1, n+1):
        for integer in range(1, n+1):
            print(number * integer, end = ' ')
        print()

multiplication_table(12)
