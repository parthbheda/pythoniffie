# A little python program in light of Hacktoberfest 2019 :)

legal_age = 21

print("-- Welcome to the Hacktoberfest bar --")

age = int(input("How old are you? "))

if age >= legal_age:
    print("Have a beer!")
elif age == 20:
    print("So close..one more year kid.")
else:
    print(f"Sorry, {age} is too young for a beer, how about a soda?")
    