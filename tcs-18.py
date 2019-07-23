#Velski buys an array A of N integer values.In 1 second he can increase value of each array element by 1.He wants each array element's value to become greater than or equal to K.Please help velski to find out the minimum time it will take,for him to do so.
#i/p:2
3 4
1 2 5
3 2
2 5 5
#o/p:3
     0

n=int(input())
for i in range(0,n):
    a,k=map(int,input().split())
    ar=list(map(int,input().split()))
    if (k-min(ar))<=0:
        print(0)
    else:
        print(k-min(ar))
#Two Strings a and b are of different lengths are given.Find the minimum number of characters which must be removed to make it an anagrams to each other.
#i/p:1
     dct
     tfd
#o/p:2        
n=int(input())
for i in range(n):
    a=input()
    b=input()
    dct={}
    for i in a:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    for i in b:
        if i in dct:
            dct[i]-=1
        else:
            dct[i]=-1
    result=0
    for i in dct.values():
        result+=abs(i)
    print(result)                
