def check_on_number_line(num):
    if num == 0:  
        print("{} is zero!".format(num)) 
    elif num > 0:  
        print("{} is a positive number!".format(num))   
    else:  
        print("{} is a negative number!".format(num)) 

def main():
    num = float(input("Enter a number: "))
    check_on_number_line(num)

if __name__ == '__main__':
    main()