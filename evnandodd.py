first=int(input("Enter starting val:"))
last=int(input("Enter last val:"))
sumOfEven=0
sumOfOdd=0
for i in range(first,last+1):
    if(i%2==0):
        sumOfEven=sumOfEven+i
    else:
        sumOfOdd=sumOfOdd+i
print("sum of even num:",sumOfEven)
print("sum of odd num:",sumOfOdd)