from datetime import datetime as dt

hour = int(dt.now().strftime("%H"))
time = dt.now().strftime("%H:%M:%S")

yourDivider = int(input("After what hour(24 Hour system) you prefer Night: "))
while not(1<=yourDivider<=23):
    print("Please enter a valid Time when your night starts")
    yourDivider = int(input("After what hour(24 Hour system) you prefer Night: "))

if(hour >= yourDivider):
    print("time is",time,".Thus it is","Night")
else:
    print("time is",time,".Thus it is","Day")