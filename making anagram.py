n=input()
n1=input()
k=[a for a in n]
l=list()
for i in n1:
    #print(i)
    if i in k:
        k.remove(i)
    else:
        l.append(i)
print(len(k)+len(l))
##input:cde,abc
##output:4(which is the count of d,e,a,b)
