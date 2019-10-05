# Simple self-explanatory if-else based program to start/stop the car

is_started = False
while True:
    command = input('>').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == 'start':
        if not is_started: 
            is_started = True
            print('Car started..ready to go!')
        else:
            print('Car already started!')
    elif command == 'stop':
        if is_started:
            is_started = False
            print('Car stopped.')
        else:
            print('Car already stopped!')
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")