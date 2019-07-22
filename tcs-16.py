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
