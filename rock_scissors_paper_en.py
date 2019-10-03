import random
import time

computer_antworten = ['Sciccors', 'Rock', 'Paper',]
end_abfrage = "y"

print("Welcome to rock, paper, sciccors")
time.sleep(1)
eingabe_spieler = input("Chose [1] Sciccor [2] Stone [3] Paper")


if eingabe_spieler == "1":
    print("You chose sciccor!")
    time.sleep(1)
    print("It's the Computers turn!")
    time.sleep(1)
    antwort_auf_schere = random.choice(computer_antworten)
    print("He's choosing")
    time.sleep(1.5)
    print(antwort_auf_schere)
    if antwort_auf_schere == 'Schere':
            time.sleep(0.5)
            print("**Its a tie!**")
    elif antwort_auf_schere == 'Stein':
        time.sleep(0.5)
        print("**You lost!**")
    else:
        time.sleep(0.5)
        print("**You won!**")
                



if eingabe_spieler == "2":
    print("You chose stone!")
    time.sleep(1)
    print("It's the Computers turn!")
    time.sleep(1)
    antwort_auf_stein = random.choice(computer_antworten)
    print("He's choosing!")
    time.sleep(1.5)
    print(antwort_auf_stein)
    if antwort_auf_stein == 'Schere':
            time.sleep(0.5)
            print("**DYou won!**")
    elif antwort_auf_stein == 'Stein':
        time.sleep(0.5)
        print("**Tie!**")
    else:
        time.sleep(0.5)
        print("**You lost!**")


if eingabe_spieler == "3":
    print("DYou chose paper!")
    time.sleep(1)
    print("It's the Computers turn")
    time.sleep(1)
    antwort_auf_papier = random.choice(computer_antworten)
    print("He's choosing")
    time.sleep(1.5)
    print(antwort_auf_papier)
    if antwort_auf_papier == 'Schere':
            time.sleep(0.5)
            print("**You lost!**")
    elif antwort_auf_papier == 'Stein':
        time.sleep(0.5)
        print("**DYou won!**")
    else:
        time.sleep(0.5)
        print("**Tie!**")
                

                
                    

    
    
