def insertion_sort(list):
    print(list)
    sorted = []
    while not len(list) == 0:
        for item in list:
            if item == min(list):
                sorted.append(item)
                list.remove(item)
    print(sorted)

list = [99, 67, 12, 0, 53]
insertion_sort(list)
