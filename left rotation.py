b,a=list(map(int,input().split()))
l=list(map(int,input().split()))
li=[]
for i in range(a,len(l)):
    li.append(l[i])
for i in range(0,a):
    li.append(l[i])
    
print(*li)
##i/p:
5 4
1 2 3 4 5
#o/p:5 1 2 3 4
