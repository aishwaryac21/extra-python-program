###Given 2 arrays, count the number of pairs in the two arrays such that each pair has a distinct sum.
##Input Format

n,m - size of array 1 and 2

a[0...n-1] - n elements of array 1

b[0...m-1] - m elements of arrray 2###

a,b=map(int,input().split())
ar1=list(map(int,input().rstrip().split()))
ar2=list(map(int,input().rstrip().split()))
count=0
l1=[]
for i in ar1:
    for j in ar2:
        if(i+j not in l1):
            count+=1
            l1.append(i+j)
print(count)        
##i/p:2 1
      3 2
      3
##o/p:2
##i/p:2 1
      3 3
      3
##o/p:1
_____________________________________________________________________________________________________________________________

##From the given array, remove an element such that the GCD(or HCF) of the remaining elements in the array becomes maximum.

Input Format

n - size of the array

a[0...n-1] - n array elements
##i/p:3
      12 15 18
##o/p:6
##exp:GCD after removing 12 -> GCD(15,18) = 3

GCD after removing 15 -> GCD(12,18) = 6

GCD after removing 18 -> GCD(12,15) = 3
Hence, the maximum posiible GCD after removing an element form the array is 6.
def gcd(a,b):
    while(a!=b):
        if(a>b): 
            a-=b
        else:
            b-=a
    return a
n=int(input())
l1=list(map(int,input().split()))
l2=[]
l3=[]
for i in range(len(l1)): 
    for j in range(len(l1)):
        if(i!=j):
            l2.append(l1[j])
    #print(l2)
    a=l2[0]
    b=l2[1]
    g=gcd(a,b)
    for k in range(2,len(l2)):
        g=gcd(g,l2[k])
    l3.append(g)
    #print(l3)
    l2.clear()
print(max(l3))
      
