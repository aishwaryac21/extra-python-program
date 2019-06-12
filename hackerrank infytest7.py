@1 ## Print Fibonacci numbers till n

def rev(string):
    if string==0:
        return 0
    else:
        return string[::-1]

a=str(input())
print(rev(a))
##i/p: computer
##o/p:retupmoc

@2 ##find the frequency of character in a string.

from collections import OrderedDict
s=input()
l=sorted(s)
d=OrderedDict()
for i in l:
    d[i]=0
for i in l:
    d[i]+=1
for i in d:
    print(i,d[i])
##i/p:welcome
##o/p:
c 1
e 2
l 1
m 1
o 1
w 1

@3 ##Convert a lowercase string to uppercase String.
string=str(input())
print(string.upper())

@4 Remove all Characters in a String except Alphabet.

string=str(input())
string1=''
let="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in string:
    if i in let:
        string1=string1+i
print(string1)

##i/p:kit21
##o/p:kit
