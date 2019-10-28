def factorial(n) : 
	fact = 1; 
	while (n != 0) : 
		fact = fact * n; 
		n = n - 1
	return fact 

def isKrishnamurthy(n) : 
	sum = 0
	temp = n 
	while (temp != 0) : 

		sum = sum + factorial( temp % 10) 

		temp = temp / 10; 
		
	return (sum == n) 

n = 145
if (isKrishnamurthy(n)) : 
	print "YES"
else : 
	print "NO"

