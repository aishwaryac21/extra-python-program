#i/p:5
#o/p:5!=120
n=int(input())
def f(n):
    fact=1
    while(n>0):
        fact=fact*n 
        n=n-1
    return fact
print(n,"!=",f(n))    
