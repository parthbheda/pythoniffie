num1 = input("Enter first num: ")
num2 = input("Enter second num: ")
num3 = input("Enter third num: ")
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print("The largest number is",largest)
