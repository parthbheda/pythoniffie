import math 
MAX = 10000; 

primes = []; 

def sieveSundaram(): 

	marked = [False] * int(MAX / 2 + 1); 

	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1): 
		for j in range((i * (i + 1)) << 1, 
					int(MAX / 2) + 1, 2 * i + 1): 
			marked[j] = True; 

	primes.append(2); 

	for i in range(1, int(MAX / 2) + 1): 
		if (marked[i] == False): 
			primes.append(2 * i + 1); 

def isEquidigital(n): 

	if (n == 1): 
		return True; 

	original_no = n; 
	sumDigits = 0; 
	while (original_no > 0): 
		sumDigits += 1; 
		original_no = int(original_no / 10); 

	pDigit = 0; 
	count_exp = 0; 
	p = 0; 
	i = 0; 
	while (primes[i] <= int(n / 2)): 
		
		while (n % primes[i] == 0): 
			
			p = primes[i]; 
			n = int(n / p); 

			count_exp += 1; 

		while (p > 0): 
			pDigit += 1; 
			p = int(p / 10); 

		while (count_exp > 1): 
			pDigit += 1; 
			count_exp = int(count_exp / 10); 
		i += 1; 

	if (n != 1): 
		while (n > 0): 
			pDigit += 1; 
			n = int(n / 10); 

	return (pDigit == sumDigits); 

sieveSundaram(); 

print("Printing first few Equidigital", 
	"Numbers using isEquidigital()"); 
for i in range(1, 20): 
	if (isEquidigital(i)): 
		print(i, end = " "); 
		
