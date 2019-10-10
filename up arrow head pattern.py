n=int(input())
x=n-1
z=1
for i in range(n):
    y=n
    print("- "*x,end="")
    for j in range(z):
        print(y,end=" ")
        if j<i:
            y-=1
        else:
            y+=1
    z+=2
    print("\r")
    x-=1