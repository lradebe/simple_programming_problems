def fibonacci_numbers(fibonaccis):

    fibonacci_numbers = []
    number1 = 0
    number2 = 1

    while not len(fibonacci_numbers) == fibonaccis:
        fibonacci_numbers.append(number1)
        nth_number = number1 + number2
        number1 = number2
        number2 = nth_number

    print(fibonacci_numbers)

fibonaccis = 100
fibonacci_numbers(fibonaccis)


