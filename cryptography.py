"""
cryptography.py
Author: Jasper
Credit: Brendan, Ethan

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
what =input( "Enter e to encrypt, d to decrypt, or q to quit: ")
i=list(input("Message: "))
inp=[associations.find(x) for x in i]
li=len(inp)
dinp=[associations.find(x) for x in i]
k=list(input("Key: "))
key=[associations.find(x) for x in k]
lk=len(key)
to=list('1'*li)
tot=list('1'*li)
j=0


if what == "e":
    while j<li:
        to[j]=int(inp[j])+int(key[j%(lk-1)])
        j=j+1
     
        to=[associations[x] for x in to]
        j=0


if what == "d":
    while j<li:
        tot[j]=int(inp[j])-int(key[j%(lk-1)])
        j=j+1
        
        tot=[associations[x] for x in tot]


















