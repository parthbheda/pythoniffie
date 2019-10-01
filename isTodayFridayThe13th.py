import datetime

'''
Inspired by https://www.reddit.com/r/IsTodayFridayThe13th/
'''

print('Is Today Friday the 13th?')

today = datetime.date.today()

if today.weekday() == 5 and today.strftime('%d') == 13:
    print('Yes.')
else:
    print('No.')
