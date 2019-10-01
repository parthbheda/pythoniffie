#-*-coding: utf8-*-

# python 2.7

x = 'Doritos'
y = 'Cake'

print 'choices =>', x, 'or', y

inpt = raw_input("type option ....: ")

inpt = inpt.lower()
x = x.lower()
y = y.lower()

if inpt == x:
	print('Great, get some sauce !')
elif inpt == y:
	print('Yeahh, get some soda !')
else:
	print('Fine... maybe later')
