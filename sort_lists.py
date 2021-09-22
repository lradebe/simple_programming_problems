def sort_lists(list1, list2):

    list1.extend(list2), list1.sort()
    print(list1)

list1 = [1, 3, 5]
list2 = [0, 2, 4, 6]
sort_lists(list1, list2)
