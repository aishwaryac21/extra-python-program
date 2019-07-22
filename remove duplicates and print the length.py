from collections import OrderedDict
def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))     
n=input()
a=remove_duplicate(n)
print(len(a))

#i/p:ABCDEFAB
#o/p:6
