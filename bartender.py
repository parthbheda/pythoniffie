# A little python program in light of Hacktoberfest 2019 :)

legalage = 21
age = int(input("How old are you? "))

if age >= legalage:
    print("Have a beer!")
else:
    print("Sorry",age," is too young for a beer, how about a soda?")
    