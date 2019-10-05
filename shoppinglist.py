import cPickle as p
einkaufsdatei = 'einkaufsliste.data' # Die Daei in die die Einkauflsite immer gespeichert werden soll

try:
    f = file(einkaufsdatei)
    gl = p.load(f)

except:
    einkaufsliste = [] # Die Liste
    f = file(einkaufsdatei, 'w')
    p.dump(einkaufsliste, f)
    f.close()
    del einkaufsliste
    f = file(einkaufsdatei)
    gl = p.load(f)


def menue(): # Das Menue
    print '- - - - - - - - - - - - - - - - - - - - - - -'
    print 'Welcome!'
    print 'Please press...'
    print '1 to view your shopping list'
    print '2 to add a product to shopping list'
    print '3 to delete a product that you already bought'
    print '4 to save your shopping list'
    print '5 to close the program'
    print '- - - - - - - - - - - - - - - - - - - - - - - '

while True:
    menue()
    option = raw_input('You choose: ')
    if option == '1':
        if len(gl) > 0:
            print 'Your shopping list contains following objects:'
            for item in gl:
                print item
        else:
            print 'DYour list is empty!'
    elif option == '2':
        neues_produkt = raw_input('Please enter the product you want to buy: ')
        gl.append(neues_produkt)
        print 'PProduct added!'
    elif option == '3':
        loesch_produkt = raw_input('Please enter the product you want to delete ')
        while loesch_produkt in gl:
            produkt_nummer = gl.index(loesch_produkt)
            del gl[produkt_nummer]
            print 'The product has been removed'
            break
        else:
            print 'The product is in your shopping list'
    elif option == '4':
        f = file(einkaufsdatei, 'w')
        p.dump(gl, f)
        f.close()
        del gl
        f = file(einkaufsdatei)
        gl = p.load(f)
        print 'Your shopping list has been saved!'
    elif option == '5':
        print 'See you soon!'
        break
    else:
        print 'Error! Choose one of the 5 options'
