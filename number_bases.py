def number_bases(list):

    binary_list = []
    for number in list:
        num = bin(number)
        binary_list.append(int(num[2:]))
    print(f'Base 1 numbers: {list}\n\nBase 2 numbers: {binary_list}')

list = [i for i in range(6)]
number_bases(list)
