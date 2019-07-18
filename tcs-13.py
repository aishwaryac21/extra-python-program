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
 #Given a number of N digits, find the sum of all possible permutations of the given n-digits.
   
    def factorial(n): 
    f = 1
    if (n == 0 or n == 1): 
        return 1
    for i in range(2, n + 1): 
        f = f * i 
    return f 
def getSum(arr, n): 
    fact = factorial(n)  
    digitsum = 0
    for i in range(n): 
        digitsum += arr[i] 
    digitsum *= (fact // n)
    res = 0
    i = 1
    k = 1
    while i <= n : 
        res += (k * digitsum) 
        k = k * 10
        i += 1
    return res 
arr =list(map(int,input())) 
n = len(arr)
print(getSum(arr, n)) 
#i/p:123
#o/p:1332{All possible permutations of the number 123 are 123, 132 , 312 , 213, 231 , 321. Sum of all permuatations is 1332.} 




