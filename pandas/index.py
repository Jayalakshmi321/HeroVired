import pandas as pd
a=[1,8,4]
myVar=pd.Series(a,index=["x","y","z"])
print(myVar)

marks=[75,80,95]
b=pd.Series(marks,index=["Hari","Durga","Jaya"])
print(b)

stuName=[input("Enter your name:")for i in range(5)]
stuMarks=[int(input("Enter your marks:"))for i in range(5)]
c=pd.Series(stuMarks,index=[stuName])
print(c)