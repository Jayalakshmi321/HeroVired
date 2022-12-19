val=int(input("enter the values:"))
n1,n2=0,1
count=0
if(val<=0):
    print("please enter a positive number")
elif val==1:
    print('fibonocci series upto ',val)
    print(n1)
else:
    print("fibonocci series")
    while(count<val):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        