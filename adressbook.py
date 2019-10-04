import cPickle as p

personendatei = 'personenliste.data' # Datei in die, die Liste nachher gespeichert werden soll.

class Person:
      '''Stellt eine Person da.'''
      def __init__(self, name, alter, position, adresse, email):
          self.name = name
          self.alter = alter
          self.position = position
          self.adresse = adresse
          self.email = email
          print 'Person %s initialisiert' % self.name

      def auskunft(self):
          '''Gibt genauere Daten über die Person aus'''
          print 'Name: "%s" Age: "%s" Position: "%s" Adress: "%s" Email: "%s"' %(self.name, self.alter, self.position, self.adresse, self.email)

try:
    f = file(personendatei)
    gl = p.load(f) # GL steht fuer GespeicherteListe

except:
    # 'Ab' steht für 'A'dress'b'uch
    ab = []

    f = file(personendatei, 'w')
    p.dump(ab, f)
    f.close()

    del ab # Loeschen des Adressbuches

    # Wieder einlesen des Adressbuches aus der Datei
    f = file(personendatei)
    gl = p.load(f) # GL steht fuer GespeicherteListe

def menu():
    print 'Welcome to your adressbook! Please press...'
    print '1 to view your adressbook!'
    print '2 to search in your adressbook'
    print '3 to add a contact'
    print '4 uto delete a contact'
    print '5 to save your changes'
    print '6 to show the menu again'
    print '7 to close the program'


menu()
while True:
    print '- - - - - - - - - - - - - - - - - - - -'
    option = raw_input('Please anter one of the options! ')
    if option == '1':
        if len(gl) > 0:
            for item in gl:
                item.auskunft()
        else:
            print 'The adressbook is empty'
    elif option == '2':
        item = raw_input('Please enter the name: ')
        for pers in gl:
            if pers.name == item:
                pers.auskunft()
                break
        else:
            print 'The name isnt in the adressbook!'
    elif option == '3':
        neu_name = raw_input('Please enter the new contact: ')
        neu_alter = raw_input('Enter the age of the contact: ')
        neu_position = raw_input('Enter ypur relation to this contact: ')
        neu_adresse = raw_input('Enter his location: ')
        neu_email = raw_input('GEnter the E-Mail of the contact: ')
        neu_name = Person(neu_name, neu_alter, neu_position, neu_adresse, neu_email)
        gl.append(neu_name)
    elif option == '4':
        item = raw_input('Please enter the name of the contact you want to delete:')
        for pers in gl:
            if pers.name == item:
                gl.remove(pers)
                print 'Contact deleted!'
                break
        else:
            print 'The name isnt in your adressbook!'
    elif option == '5':
        f = file(personendatei, 'w')
        p.dump(gl, f)
        f.close()
        print 'Succesfully saved!'
    elif option == '6':
        menu()
    elif option == '7':
        print 'See you!'
        break
    else:
        print 'Please enter your option again!'
