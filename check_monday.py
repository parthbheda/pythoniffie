import datetime



print('Is Today Monday?')

today = datetime.date.today()

if today.weekday() == 1:
    print('Yes.')
else:
    print('No.')
