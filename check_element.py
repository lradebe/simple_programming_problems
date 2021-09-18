def check_element(element, mylist):

    not_founds = []

    while isinstance(element, str) is True:
        for item in mylist:
            if item.find(element):
                continue
            else:
                print('Found: ', item)
        break

    while isinstance(element, int) is True:
        for item in mylist:
            if item is element:
                print('Found', item)
            else:
                not_founds.append(item)
            if len(mylist) == len(not_founds):
                print('Not Found')
        break

mylist = [1,2,3,4,5]
check_element(4, mylist)
