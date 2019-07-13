n=int(input())
m=int(input())
sum=0
ar=[[0]*m]*n
ar=[[int(input())for i in range(m)]for j in range(n)]
if m<=2 and n<=2:
    sum=-1
else:
    for k in range(n):
        for l in range(m):
            if k==0 or l==0 or k==n-1 or l==m-1:
                pass
            else:
                sum+=ar[k][l]
print(sum)                
