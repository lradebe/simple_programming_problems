def sum_or_product():

    SUM = 0
    PRODUCT = 1
    number = int(input('Enter number: '))
    chosen_option = input('SUM of given number or PRODUCT? ')

    if chosen_option == 'SUM' or chosen_option == 'sum' or chosen_option == 'Sum':
        for integer in range(1, number+1):
            SUM += integer
        print(SUM)

    elif chosen_option == 'PRODUCT' or chosen_option == 'Product' or chosen_option == 'product':
        for integer in range(1, number+1):
            PRODUCT *= integer
        print(PRODUCT)

sum_or_product()

