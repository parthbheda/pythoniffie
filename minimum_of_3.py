a = input("Enter first num")
b = input("Enter second num")
c = input("Enter third num")
if a > c and b > c:
    print(str(c)+" is smallest.")
elif a > b and c > b:
    print(str(b)+" is smallest.")
else:
    print(str(a)+" is smallest.")
