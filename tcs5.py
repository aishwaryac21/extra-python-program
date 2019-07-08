##Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#i/p:1 3 5 4 7
#o/p:3

def lenOfLongIncSubArr(arr, n) :  
    m = 1
    l = 1
    for i in range(1, n) : 
        if (arr[i] > arr[i-1]) : 
            l =l + 1
        else :  
            if (m < l) : 
                m = l 
            l = 1
    if (m < l) : 
        m = l 
    return m 
arr =[int(i) for i in input().split()]
#print(arr)
n = len(arr) 
print(lenOfLongIncSubArr(arr, n)) 
