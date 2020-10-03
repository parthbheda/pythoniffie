from datetime import datetime as dt

hour = int(dt.now().strftime("%H"))
time = dt.now().strftime("%H:%M:%S")

if(hour >= 19):
    print("time is",time,".Thus it is","Night")
else:
    print("time is",time,".Thus it is","Day")