#Given a number n, find the val after n occurences of the given sequence
#(1/1!)+(2/2!)+(3/3!)+.....+(n/n!)
#i/p:5
#o/p:2.708333

n=int(input())
def f(n):
    fact=1
    while(n>0):
        fact=fact*n 
        n=n-1
    return fact
s=1
for i in range(2,n+1):
    s+=i/f(i)
print('%.6f' %s)   

#Given a sequence of length n, find the length of longest progressive sub-sequence present in the given sequence.
#i/p:5
     1 1 2 1 2
#o/p:3
def lenOfLongIncSubArr(arr, n) :  
    m = 1
    l = 1
    for i in range(1, n) : 
        if (arr[i] >=arr[i-1]) : 
            l =l + 1
        else :  
            if (m < l) : 
                m = l 
            l = 1
    if (m < l) : 
        m = l 
    return m 
n=int(input())
arr =list(map(int,input().split()))
print(lenOfLongIncSubArr(arr, n)) 

#Given a Roman number convert it into Decimal number
#i/p:XVII
#o/p:17
def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val
n=input()
print(roman_to_int(n))

