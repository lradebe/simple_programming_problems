def number_pattern(number):

    for num in range(number):
        print(str(num) * len(range(num)))
    print()

if __name__ == '__main__':
    number = 4
    number_pattern(number)
