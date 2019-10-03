import random
import time

computer_antworten = ['Schere', 'Stein', 'Papier',]
end_abfrage = "y"

print("Willkommen zu Schere, Stein, Papier")
time.sleep(1)
eingabe_spieler = input("Wähle [1] Schere [2] Stein [3] Papier")


if eingabe_spieler == "1":
    print("Du hast Schere ausgewählt!")
    time.sleep(1)
    print("Nun wählt der Computer!")
    time.sleep(1)
    antwort_auf_schere = random.choice(computer_antworten)
    print("Er wählt:")
    time.sleep(1.5)
    print(antwort_auf_schere)
    if antwort_auf_schere == 'Schere':
            time.sleep(0.5)
            print("**Unentschieden!**")
    elif antwort_auf_schere == 'Stein':
        time.sleep(0.5)
        print("**Du hast Verloren!**")
    else:
        time.sleep(0.5)
        print("**Du hast Gewonnen!**")
                



if eingabe_spieler == "2":
    print("Du hast Stein ausgewählt!")
    time.sleep(1)
    print("Nun wählt der Computer!")
    time.sleep(1)
    antwort_auf_stein = random.choice(computer_antworten)
    print("Er wählt:")
    time.sleep(1.5)
    print(antwort_auf_stein)
    if antwort_auf_stein == 'Schere':
            time.sleep(0.5)
            print("**Du hast Gewonnen!**")
    elif antwort_auf_stein == 'Stein':
        time.sleep(0.5)
        print("**Unentschieden!**")
    else:
        time.sleep(0.5)
        print("**Du hast verloren!**")


if eingabe_spieler == "3":
    print("Du hast Papier ausgewählt!")
    time.sleep(1)
    print("Nun wählt der Computer!")
    time.sleep(1)
    antwort_auf_papier = random.choice(computer_antworten)
    print("Er wählt:")
    time.sleep(1.5)
    print(antwort_auf_papier)
    if antwort_auf_papier == 'Schere':
            time.sleep(0.5)
            print("**Du hast Verloren!**")
    elif antwort_auf_papier == 'Stein':
        time.sleep(0.5)
        print("**Du hast Gewonnen!**")
    else:
        time.sleep(0.5)
        print("**Unentschieden!**")
                

                
                    

    
    
