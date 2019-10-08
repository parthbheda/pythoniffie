n=input()
l=len(n)
x=l-1
for i in range(l):
    if n[x]=='0':
        print('-')
    else:
        print(n[i]*int(n[x]))
    x-=1