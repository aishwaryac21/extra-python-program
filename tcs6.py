#Given an array A of N positive integers. The task is to swap every ith element of the array with (i+2)th element.
length=int(input())
list1=list(map(int,input().rstrip().split()))
for i in range(0,len(list1)-2):
    list1[i],list1[i+2]=list1[i+2],list1[i]
for i in list1:
    print(i,end=' ')
   ##i/p:5
         1 2 3 4 5
   ##o/p:3 4 5 2 1

##Print the maximum sum of the non-contiguous subarrays of the given array.
num1=int(input())
list1=list(map(int,input().rstrip().split()))
sum=0
for i in list1:
    if sum+i>sum:
        sum+=i
print(sum)
##i/p:5
      9 -8 5 -2 7
##o/p:21(9+5+7)
