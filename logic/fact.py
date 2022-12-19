num=int(input("enter a number:"))
fact=1
if(num<0):
    print("please enter a positive number:")
elif(num==0):
    print("Factorial of zero is one")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"The factorial of {num} is:",fact)
