import datetime

print('Is Today Monday?')

today = datetime.date.today()

# today.weekday() output:
# Sunday  = 0
# Monday  = 1
# Tuesday = 2
# ...

if today.weekday() == 1:
    print('Yes.')
else:
    print('No.')
