"""
cryptography.py
Author: Jasper
Credit: Brendan

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
i=list(input("Message: "))
inp=[associations.find(x) for x in i]
li=len(inp)
k=list(input("Key: "))
key=[associations.find(x) for x in k]
lk=len(key)
to=list('1'*li)
j=0
p=0

while p<li:
    to[j]=int(inp[p])+int(key[j])
    j=j+1
    p=p+1
    if j==lk-1:
        j=0



print (to)

















