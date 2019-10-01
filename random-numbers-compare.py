#-*-coding: utf8-*-
#python 2

from random import randint as rand

x = rand(1, 20)
y = rand(1, 20)

if x > y:
	print 'x > y (x => {0}, y => {1})'.format(x, y)
elif x < y:
	print 'x < y (x => {0}, y => {1})'.format(x, y)
else:
	print 'x = y (x => {0}, y => {1})'.format(x, y)
