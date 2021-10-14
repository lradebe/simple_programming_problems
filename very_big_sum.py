def very_big_sum(array, num):
    Array = array.copy()
    print(f'Old Array: {array}\n')
    while len(Array) != len(range(num)):
        for number in array:
            for integer in Array:
                if number == array[-1]:
                    y = len(range(num)) - len(Array)
                    number += y;
                    Array.append(number)
    Array = sorted(Array)
    sum = 0
    print(f'New Array: {Array}\n')
    for item in Array:
        sum += item
    print(f'Sum of elements in New Array:	{sum}')

num = 10
array = [1, 2, 3, 4, 5]
very_big_sum(array, num)
