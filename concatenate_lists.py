def concatenate_lists(list1, list2):

    print('List2 before:',list2)
    list2.extend(list1)
    print('List2 after:',list2)

list1 = [ 1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
concatenate_lists(list1, list2)
