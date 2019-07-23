#Given a set of opening and closing brackets '(' and ')'. Find the length of the longest valid brackets.
#i/p:((()
#o/p:2
#i/p:()(((()())
#o/p:6--The longest valid brackets are '(()())'. Length is 6.
###16a:
n=input()
l=len(n)
s=[]
s.append(-1)
c=0
for i in range(l):
    if(n[i]=='('):
        s.append(i)
    else:
        s.pop()
        if(len(s)!=0):
            c=max(c,i-s[len(s)-1])
        
        else:
            s.append(i)
print(c)
#An integer N is given, find the total number of number 1 appearing in the range 0->N.
#i/p:13
#o/p:6(Total number of 1's from 0 to 13 is 6. The occurence of 1 are in the numbers 1,10,11,12,13)

n=int(input())
count=0
for i in range(1,n+1):
    a=str(i)
    if("1" in a):
        count+=a.count("1")
print(count)        
