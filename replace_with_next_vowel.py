#Get a string and char which has to be replaced
#input:
# accuracy c
#output:
# auuuracy
# After the char 'c' the next occuring vowel is 'u' therefore the initial 'c's are
# replaced with 'u' but for the final 'c' there are no vowels after therefore it
# is left as it is 
s,c=map(str,input().split());s=list(s)
vow="aeiou";order=[];l=len(s)
for i in range(l):
    if s[i] in vow:
        order.append(s[i])
for i in range(l):
    if s[i] in order:
        del order[0]
    if s[i]==c:
        if len(order)>0:
            s[i]=order[0]
print(*s,sep="")        