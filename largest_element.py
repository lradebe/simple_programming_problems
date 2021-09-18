def largest_element(mylist):

    largest_element = 0
    for element in mylist:
        if element >= largest_element:
            largest_element = element
    print(largest_element)

largest_element([1, 2, 3, 4, 5])
