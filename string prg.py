###  Alternating Characters  ###
t=int(input())
for _ in range(t):
    del_cut=0
    s=input()
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            del_cut+=1
    print (del_cut)   
