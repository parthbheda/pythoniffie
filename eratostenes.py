import sys

primes=[2, 3]
 
i, j, k = 5, 0, 0

while i<100000:
 
   j = 0
   k = i**(0.5)
 
   while primes[j]<k and i%primes[j]:
      j += 1

   if primes[j]>k:
      primes += [i]

   if i%3==2:
      i+=2
   else:
      i+=4
 
for j in primes:
   sys.stdout.write("%d " %j)

print
