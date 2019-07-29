#Given a number n, find whether the given number is a strong number or not. A Strong number is the a number in which the sum of factorials of all the digits of the given number is equal to the same number .
#i/p:145
#o/p:YES(1!+4!+5!=1+24+120=145,is called as strong number)

n=int(input())
a=0
t=n
def fact(num):
    f=1
    while(num>0):
        f=f*num
        num=num-1
    return f
while(t>0):
    b=t%10
    a+=fact(b)    
    t=t//10
if (a==n):
    print("YES",end='')
else:
    print("NO",end='')
   
#Given two numbers m and n, find the sum of all prime numbers in the range(m,n).
#i/p:1 10
#o/P:18(1+2+3+5+7=18)

a,b=map(int,input().split())
sum=0
for num in range(a,b+1):
        for i in range(2, (num//2)+1):
            if(num%i)==0:
                break
        else:
            sum+=num
            #print(num)
print(sum)
   
    
