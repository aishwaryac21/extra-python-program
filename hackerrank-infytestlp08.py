##balanced brackets:
s=str(input())

count1 = s.count("(")
count2=s.count(")")
if(s[len(s)-1]=="("):
    print("-1")
elif(count1==count2):
    print(count1)
else:
    print("-1")
    
#i/p:(())(())
#o/p:4
#i/p:()()(
#o/p:-1
