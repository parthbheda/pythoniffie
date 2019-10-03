import sys

def generate_fibonacci(num): 
    if num <=  1 :  
        return num  
    else :  
        return (generate_fibonacci (num - 2 ) + generate_fibonacci (num - 1 ))

def main():
    terms =  int ( input ( " How many terms? " ))  
    if terms <=  0 :  
        print("Enter more than 0 terms!")
        sys.exit()
    else :  
        print("Fibonacci sequence for {} terms is: ".format(terms))
    for term in  range (terms):  
        print (generate_fibonacci (term))

if __name__ == '__main__':
    main()