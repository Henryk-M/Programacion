nums=input()
nlist=nums.split(" ")

max1=int(nlist[0])
max2=int(nlist[1])
max3=int(nlist[2])

if max1>max2 and max1>max3:
    print(max1)
if max2>max1 and max2>max3:
    print(max2)
if max3>max1 and max3>max2:
    print(max3)

