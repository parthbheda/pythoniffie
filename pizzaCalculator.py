import math
people = int(input('How many people? '))

pizza = 1.5

ergebnis = int(round(people * pizza))

if people >= 10:
    ergebnis = ergebnis +1
    print(math.ceil(ergebnis))
else:
    print(math.ceil(ergebnis))
