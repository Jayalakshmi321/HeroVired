#for numbers

num=int(input())
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print(f"{temp} is a palindrome")




#for string

"""str=input()
rev=str[::-1]
if str==rev:
    print("palindrome")
else:
    print("not a palindrome!")"""