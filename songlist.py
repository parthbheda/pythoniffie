import cPickle as p
liederdatei = 'liederliste.data' # Datei in welche später die Liederliste gespeichert werden soll

class song:
    def __init__(self, name, interpret):
        self.name = name
        self.interpret = interpret
        print 'Song will be initialized'
    def auskunft(self):
        print 'Interpreter: "%s" Title: "%s"' %(self.interpret, self.name)
try:  # Der Versuch die Datei zu laden und ...
    f = file(liederdatei)
    gl = p.load(f)
except:  # ...falls sie noch nicht vorhanden ist, die Erstellung
    ld = [] # ld steht fuer 'L'ieder'L'iste
    f = file(liederdatei, 'w')
    p.dump(ld, f)
    f.close()
    del ld
    f = file(liederdatei)
    gl = p.load(f)

def menue():    # Das Menue
    print 'Welcome to your song list'
    print 'Please press..'
    print '1 to view your song list'
    print '2 to search a song'
    print '3 to add a song
    print '4 to delete a song from your list'
    print '5 to save your list'
    print '6 to close the program'
menue()   
while True:
    print '- - - - - - - - - - - - - - - - - - - - - -' # Aus Schoenheitsgruenden in der IDLE diese Reihe
    option = raw_input('Please enter your option: ')
    if option == '1':
        if len(gl) > 0:
            print 'There are %d Lsongs in your list:' % len(gl)
            for lied in gl:
                lied.auskunft()
        else:
            print 'IYour list is empty'
    elif option == '2':
        such_name = raw_input('Please enter the interpreter of the song youre searching for: ')
        for lied in gl:
            if such_name == lied.name or lied.interpret:
                lied.auskunft()
            else:
                print 'SThis song isnt available!'
    elif option == '3':
        neu_lied = raw_input('Please enter the name of the song you want to add: ')
        neu_interpret = raw_input('Please enter the name of the interpreter: ')
        neu_lied = song(neu_lied, neu_interpret)
        gl.append(neu_lied)
    elif option == '4':
        del_name = raw_input('Please enter the name of the song you want to delete: ')
        for lied in gl:
            if del_name == lied.name:
                gl.remove(lied)
                print 'Song deleted!'
                break
            else:
                print 'SThe song isnt in your list!'
    elif option == '5':
        f = file(liederdatei, 'w')
        p.dump(gl, f)
        f.close()
        print 'Saved!'
        f = file(liederdatei)
        gl = p.load(f)
    elif option == '6':
        print 'See you soon!'
        break
    else:
        print 'Error! Please enter a number between 1-5'
