n,r=map(int,input().split())

if (1<=n<=1000) and (1300<=r<=1501) :

    for i in range(n):
        a=int(input())
        if (1300<=a<=1501):
            
            if a<r:
                print("Bad boi")
                break
            elif a>=r:
                print("Good boi")
                break
