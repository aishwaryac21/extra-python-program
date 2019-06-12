##ARMSTRONG NO BETWEEN TWO INTERVAL
low=int(input())
upp=int(input())
for num in range(low,upp+1):
    a=len(str(num))
    sum=0
    temp=num
    
    while temp>0:
        digit=temp%10
        sum+=digit**a
        temp//=10
    if num==sum:
        print(sum)
        
        
    
        
