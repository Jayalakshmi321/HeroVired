def changeNum(myList):
    myList.append([1,2,3,4])
    print("values inside the function",myList)
    return

myList=[40,50,60,70]
print("values outside the function",myList)
changeNum(myList)
