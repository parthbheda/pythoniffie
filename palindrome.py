def main():
    inp = input(str('Please introduce your word or sentence:\n'))
    inp = inp.lower()
    reverse = inp[::-1]

    if( inp == reverse ):
        print('Palindrome!!!')
    else:
        print('Not palindrome... :(')

main()
