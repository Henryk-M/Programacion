numa=input()
numl=[]
div=0
rem=0
numl=numa.split(" ")
if int(numl[1])>0:
    div=int(numl[0])//int(numl[1])
    rem=int(numl[0])%int(numl[1])
    divd=round(div) 
    print(divd, rem)
   