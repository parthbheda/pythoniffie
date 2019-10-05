# Check inventory with an array

inventory = ['Apple', 'Banana', 'Orange']

print('You have:')
print('- {0}'.format('\n- '.join(inventory)))

if input('What do you want to check for? ') in inventory:
    print("Yep, that's in your inventory.")
else:
    print("That's not in your inventory!")
