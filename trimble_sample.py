##closest number in an array::
a=list(map(int,input().split()))
n=int(input())
b=a[0]
for i in range(len(a)):
    if abs(n-a[i]) < abs(n-b):
        b=a[i]
print(b)      
