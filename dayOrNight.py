from datetime import datetime as dt

hour = int(dt.now().strftime("%H"))

if(hour >= 19):
    print("Night")
else:
    print("Day")