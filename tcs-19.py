#Given an array of size n, containing 1's and 0's. Find the minimum number of swap operations to be performed to group all the 1's together.
#i/p:5
#     1 0 1 0 1
#o/p:1

n=int(input())
arr=list(map(int,input().split()))
Ones = 0
for i in range(0, n) : 
    if (arr[i] == 1) : 
        Ones = Ones + 1
x = Ones 
count_ones = 0
maxOnes = 0
for i in range(0, x) : 
    if(arr[i] == 1) : 
        count_ones = count_ones + 1 
maxOnes = count_ones 
for i in range(1, (n - x + 1)) : 
    if (arr[i - 1] == 1) : 
        count_ones = count_ones - 1
    if(arr[i + x - 1] == 1) : 
        count_ones = count_ones + 1
        
    if (maxOnes < count_ones) : 
            maxOnes = count_ones 
zeroes = x - maxOnes    
print(zeroes) 
