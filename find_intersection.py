def find_intersection(Array):
    '''This function takes in a list with two strings \
it must return a string with numbers that are found on \
both list elements. If there are no common numbers between \
both elements, return False'''

    first = list(Array[0].split(', '))
    second = list(Array[1].split(', '))
    string = ''
    both = []

    for number in first:
        if number in second:
            both.append(number)
    sorted(both)
    if len(both) == 0:
        return False
    for number in both:
        if not number == both[-1]:
            string += f'{number}, '
        else:
            string += f'{number}'
    print(string)

Array = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
find_intersection(Array)
