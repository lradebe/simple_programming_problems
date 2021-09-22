def alternating_lists(list1, list2):

    list3 = []
    for item in list1 :
        for object in list2:
            if list1.index(item) == list2.index(object):
                list3.append(item)
                list3.append(object)
    print(list3)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
alternating_lists(list1, list2)
