#Write a program that reads two numbers and prints their maximum.
nums=input()
nlist=nums.split(" ")
maxim=0
execute="s"

if int(nlist[0])>int(nlist[1]):
    print(nlist[0])
if int(nlist[0])<int(nlist[1]):
    print(nlist[1])    
if int(nlist[0])==int(nlist[1]):
    print(int(nlist[1]))    
