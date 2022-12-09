""""
# WAY-1

val=list(map(int,input().split()))
sum=0
for i in val:
    if i<=0:
        print("Please enter positive numbers!")
    else:
        sum=sum+i
        x=open("output.txt",'a')
        print("Entered values are:",i,file=x)
print("Total sum:",sum)
print("Total sum:",sum,file=x)
        
"""""

#WAY-2

input1=int(input("Enter value1-"))
input2=int(input("Enter value2-"))
input3=int(input("Enter value3-"))
input4=int(input("Enter value4-"))
input5=int(input("Enter value5-"))
val=[input1,input2,input3,input4,input5] 
sum=0
for i in val:
    if i<=0:
        print("Please enter positive numbers!")
    else:
        sum=sum+i
        x=open("output.txt",'a')
        print("Entered values are:",i,file=x)
print("Total sum:",sum)
print("Total sum:",sum,file=x)
