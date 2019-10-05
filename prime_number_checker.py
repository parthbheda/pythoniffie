
prime = int(input("What number do you wanna check?"))

if prime > 1 :
    for i in range(2,prime):
        if (prime % i) == 0:
            print("Your number is not a prime number")
            print("Because "+str(prime)+" divided by "+str(i)+" is 0.")
            break
        else:
            print(prime,"is a prime number")
            break
else:
    print(prime, "is not a prime number")