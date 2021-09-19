def odd_index(mylist):

    for item in mylist:
        if mylist.index(item) % 2 != 0:
            return item

mylist = ['a','b','c','d','e']
odd_index(mylist)
