#Data frame is a multi dimensional array
import pandas as pd
Entries={
    "Temparature":[99,100,102,98,80],
    "Days":["Mon","Tue","Wed","Thu","Fri"]
}
df=pd.DataFrame(Entries)
# print(df)
print(df.loc[0])
