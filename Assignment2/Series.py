#Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 

import pandas as pd
l=[]
for i in range(5):
    n=int(input())
    l.append(n**2)
pow=pd.Series(l)
print(pow)