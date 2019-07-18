#Sort an array in ascending order leaving the negative elements in their present position.

n=int(input())
a=list(map(int,input().rstrip().split()))
ans=[] 
for i in range(n): 
    if (a[i] >= 0): 
        ans.append(a[i]) 
ans = sorted(ans) 
j = 0
for i in range(n): 
    if (a[i] >= 0): 
        a[i] = ans[j] 
        j += 1
for i in range(n): 
    print(a[i],end = " ")
    #i/p:6
        -34 15 -39 9 21 -48
    #o/p:-34 9 -39 15 21 -48    


