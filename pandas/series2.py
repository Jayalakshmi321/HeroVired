import pandas as pd
calories={"Day1":540,"Day2":420,"Day3":460,"Day4":550,"Day5":660}
check=pd.Series(calories,index=["Day1","Day5"])
print(check)
