import pandas as pd


df = pd.read_csv("student_records.csv")
#filtering = keeping the rows that match a condition
# filter_CGPA = df[df["CGPA"] >= 3.5]
filter_cse = df[(df["Department"] == "CSE") & (df["Semester"]== 1)]




print(filter_cse)