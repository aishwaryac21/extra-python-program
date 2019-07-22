#Given an array of size n, find the sub-array with the maximum product and print the product.(The array will also contain negative elements)
#i/p:5
#     4 -10 -4 8 -1
#o/p:1280

n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(1,1<<n):
    pro=1
    for j in range(n):
        if ((i & (1 << j)) > 0):
            pro*=a[j]
           
    res=max(res,pro)
print(res)
