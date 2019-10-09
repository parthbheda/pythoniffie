# Check whether two string is anagram of each other

def anagram(a, b):
    x = ''.join(sorted(a.lower())).strip()
    y = ''.join(sorted(b.lower())).strip()

    if len(x) != len(y) or x != y:
        print('"{}" is not an anagram to "{}"'.format(a, b))
    else:
        print('"{}" is an anagram to "{}"'.format(a, b))

if __name__ == '__main__':
    a = "Tom Marvolo Riddle"
    b = "I am Lord Voldemort"
    anagram(a, b)
