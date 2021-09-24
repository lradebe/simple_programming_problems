def rotate_list(list, k):
    print(list)
    list = list[k:] + list[:k]
    print(list)

list = [1, 2, 3, 4, 5, 6]
rotate_list(list, k=2)
