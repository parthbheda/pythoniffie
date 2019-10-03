# This script checks if a number is given year is leap.

def check_leap_year():
    year_input = int(input('Enter the year: '))
    if (year_input % 4) == 0:  
        if (year_input % 100) == 0:  
            if (year_input % 400) == 0:  
                print("Yay! {} is a leap year.".format(year_input))  
            else:  
                print("Oops! {} is not a leap year.".format(year_input))  
        else:  
            print("Yay! {} is a leap year.".format(year_input))  
    else:  
        print("Oops! {} is not a leap year.".format(year_input))  

def main():
    check_leap_year()

if __name__ == '__main__':
    main()