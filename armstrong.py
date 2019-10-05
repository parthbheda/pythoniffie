# This script checks if a number is an Armstrong number.
# A number is an Armstrong number if it is equal to the sum of cubes of its digits.

def check_armstrong_number():
    number = int(input('Please enter a number: '))
    total = 0
    temp_num = number

    while(temp_num > 0):
        digit = temp_num%10
        total+=digit**3
        temp_num//=10
    
    if number == total:
        print("Yay! {} is an Armstrong number.".format(number))
    else:
        print("Oops {} is not an Armstrong number.".format(number))

def main():
    check_armstrong_number()

if __name__ == '__main__':
    main()