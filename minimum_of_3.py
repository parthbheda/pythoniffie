a = input("Enter first num:")
b = input("Enter second num:")
c = input("Enter third num:")
if a > c and b > c:
    print(str(c)+" is smallest.")
elif a > b and c > b:
    print(str(b)+" is smallest.")
elif b > a and c > a:
    print(str(a)+" is smallest.")
elif a == b and a == c:
    print(str(a)+" is equal to b or c")
elif b == a and b = c:
    print(str(b)+" is equal to a or c")
elif c == a and c == b:
    print(str(c)+" is equal to b or a")
    
