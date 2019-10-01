
#Given a number n prints the numbers from 1 to 20.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.
n=21
for i in range(1,n):
	if i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')
	elif i % 5 == 0:
		print('Buzz') 
	elif i % 3 == 0:
		print('Fizz')
	
	else:
		print(i)
	
