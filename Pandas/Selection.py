import pandas as pd

df = pd.read_csv("student_records.csv")

#SELECTION BY COLUMN
# print(df["Name"])
# print(df["CGPA"])
# print(df["Department"])
# print(df["StudentID"])
# print(df[["StudentID", "Name", "Department"]].to_string())


#SELECTION BY ROWS
print(df.loc[0])
