def palindrome_check(string):

    if string[::-1] == string:
        print('Palindrome.')
    else:
        print('Not a Palindrome.')

string = 'huh'
palindrome_check(string)
