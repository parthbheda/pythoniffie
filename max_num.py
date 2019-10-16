# program to find the max number in all the numbers taken as input
n   = int(input("Please enter the total numbers "))
max_number = 0
number_array = []
for i  in range(n):
    number_array.append(int(input()))
# numbers are taken, finding max num

for i in range(n) :
    if(number_array[i]>max_number):
        max_number = number_array[i]
    else:
        pass
print("Maximum number in the array is ",max_number)


