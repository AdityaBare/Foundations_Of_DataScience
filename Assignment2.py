import pandas as pd
import numpy as np


df = pd.read_csv("treatments.csv")

print(df.head) # Print first 5 rows of dataset
print(df.tail) # Print  last 5 rows of dataset
print(df.describe) 

print("Type : ",type(df))

print(pd.DataFrame(df))


# Print first 3 row

print(df.head(3))
print(df.tail(3))
print(df.info)

print(df.loc[0:5,["appointment_id","treatment_type"]])

print(df[df["treatment_type"]=="Standard procedure"])

print(df.shape)

print(df.iloc[3:10,1:3])