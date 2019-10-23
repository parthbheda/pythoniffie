from turtle import *
#turtle is a drawing library

# To make a square we have to move forward then a direction 4 times.

for i in range(4): # Start a loop
    forward(100) # Move forward
    right(90)  # Turn

# Now we just need to make a circle by a square
# To make it easy for us let us make a function to the square

def square():
    for i in range(4):
        forward(100)
        right(90)
        speed(0)
#     return None

for i in range(360):
    square()
    right(1)
    speed(0)

# And if you want to speed up stuff and get the result faster
# speed(10) # 0 is the fastest while 1 is the slowest, 10 is fast

# Have fun and try out different challenges