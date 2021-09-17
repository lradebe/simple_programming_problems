def prime_numbers(number):

    primes = []
    for num in range(1,number+1):
        if num > 1:
            for integer in range(2, num):
                if num % integer == 0:
                    break
            else:
                primes.append(num)
    print(f'The following is a list of prime numbers derived from the given number:\n{primes}')

prime_numbers(15)

