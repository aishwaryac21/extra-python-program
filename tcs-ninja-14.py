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
#Find the length longest substring of the given string which ha sno repeating characters.
#i/p:ABDEFGABEF
#o/p:6
#i/p:ydjofwoqwv
#o/p:6
def subst(string): 
    n = len(string) 
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0
    for i in range(1, n):
        if string[i] not in pos:  
            pos[string[i]] = i
        else: 
            if pos[string[i]] >= st:
                currlen = i - st  
                if maxlen < currlen:  
                    maxlen = currlen  
                    start = st 
                st = pos[string[i]] + 1
            pos[string[i]] = i  
    if maxlen < i - st:  
        maxlen = i - st  
        start = st 
    return len(string[start : start + maxlen])
    
string=input("")   
print(subst(string))

