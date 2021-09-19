def running_total(mylist):

    running_total = 0
    for number in mylist:
        running_total += number
    print(running_total)

mylist = [1, 2, 3, 4,5]
running_total(mylist)
