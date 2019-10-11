
print(('='*9)+'Speed Limit Program'+('='*9))

def check_speed_limit(speed):
    limit = 70
    point = 0
    if speed > limit:
        point = int((speed - limit)/5)
        if point >= 12:
            print('License Suspened')
        else:
            print('Point : '+str(point))
    else:
        print('Ok.')
        
repeat = True
while repeat:
    try:
        speed = eval(input('Speed : '))
        check_speed_limit(speed)
        repeat = False
    except NameError:
        print('Input number only!')