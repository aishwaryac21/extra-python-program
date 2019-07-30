#Given 3 strings, do the following operations

#In the first string, replace all vowels with '%'.

#In the second string, replace all consonants wiht '#'.

#In the third string, convert the string to upper case.

#Concatenate the resultant strings and display the output as a single string
'''i/p=enter
the
dragon
o/p:%nt%r##eDRAGON
'''
a=input()
b=input()
c=input()
ar=["a","e","i","o","u"]
for i in a:
    if i in ar:
        a=a.replace(i,"%")
for i in b:
    if i not in ar:
        b=b.replace(i,"#")
c=c.upper()
print(a+b+c)
