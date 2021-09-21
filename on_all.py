import math
def on_all(list):
    perfect_squares = []
    for num in list:
        if math.sqrt(num) % 1 == 0:
            if not len(perfect_squares) == 20:
                perfect_squares.append(num)
    print(perfect_squares)

list = [i for i in range(500)]
on_all(list)
