def longest_word(myString):

    new_list = []
    space = ' '
    punctuation = '\|/[]{}<>:+_)(*&^%$#@!~\'"",=-`'
    for string in myString:
        if string in punctuation or string in space:
            myString = myString.replace(string, ' ')
            new_list = myString.split(' ')
        else:
            new_list = myString.split(' ')
    return(max(new_list, key = len))


if __name__ == '__main__':

    myString = 'a confusing /:sentence:/[ this is not!!!!!!!~'
    print(longest_word(myString))
