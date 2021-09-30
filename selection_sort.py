def selection_sort(list):
    half = (len(list) // 2)
    half1 = sorted(list[:half])
    half2 = sorted(list[half:])
    sort = []
    print(list)
    for item in half1:
        for object in half2:
            if half1.index(item) == half2.index(object):
                sort.append(item)
                sort.append(object)
    print(sort)

list = [67, 9, 23, 12, 90, 32]
selection_sort(list)
