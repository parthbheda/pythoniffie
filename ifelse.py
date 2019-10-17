first = input('give first number: ')
second = input('give second number: ')

max=0
min=0
if first> second:
    max=first
    min=second
else:
    max=second
    min=first
print('max is: '+ max)
print('min is: '+ min)


