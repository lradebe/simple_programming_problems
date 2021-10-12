def quick_sort(list):
    list = sorted(list)
    half = int(len(list)/2)
    list1 = list[:half]
    list2 = list[half:]


    #print(f'{list}\n\n{list1}\n\n{list2}')


list = [79, 23, 1, 78, 55, 108]
quick_sort(list)
