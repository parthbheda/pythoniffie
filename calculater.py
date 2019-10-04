def menue():
    print Welcome to your calculater'
    print 'Please press ...'
    print '1 to add up 2 numbers'
    print '2 to subtract 2 numbers'
    print '3 to multiplicate 2 numbers'
    print '4 to divide 2 numbers'
    print '5 uto close the program'
   
while True:
    menue()
    option = raw_input('Please enter your choice!: ')
    if option == '1':
        zahl_eins = input('Please enter the first number: ')
        zahl_zwei = input('Please enter the second number: ')
        ergebnis_summe = zahl_eins + zahl_zwei
        print 'Das Ergebnis ist %s' % ergebnis_summe
    if option == '2':
        zahl_eins = input('Please enter the first number: ')
        zahl_zwei = input('Please enter the second number: ')
        ergebnis_differenz = zahl_eins - zahl_zwei
        print 'Das Ergbnis ist %s' % ergebnis_differenz
    if option == '3':
        zahl_eins = input('lease enter the first number:  ')
        zahl_zwei = input('Please enter the second number: ')
        ergebnis_produkt = zahl_eins * zahl_zwei
        print 'Das Ergbnis ist %s' % ergebnis_produkt
    if option == '4':
        zahl_eins = input('Please enter the first number: ')
        zahl_zwei = input('Please enter the second number: ')
        ergebnis_dividieren = zahl_eins / zahl_zwei
        print 'Das Ergebnis ist %s' % ergebnis_dividieren
    if option == '5':
        print 'Auf Wiedersehn'
        break 
