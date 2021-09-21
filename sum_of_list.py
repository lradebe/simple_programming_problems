sum = 0

def for_sum_of_list(list):
    global sum
    for number in list:
        sum += number
    print(sum)

def while_sum_of_list(list):
    global sum
    for number in list:
        while number != list[-1] or number is list[-1]:
            sum += number
            break
    print(sum)

def recursive_sum_of_list(list):
    i = 0
    print(list[i])
    for item in list:
        if not item == list[-1]:
            i += 1
            print(list[i])
        if item == list[-1]:
            exit()
    recursive_sum_of_list(list)


list = [1, 2, 3, 4, 5]
recursive_sum_of_list(list)
