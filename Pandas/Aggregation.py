import pandas as pd

#aggregate functions = Reduces a set of values 
                    # into a single summary value used to summarize 
                    # and analyze data often used with the groupby() function


df = pd.read_csv("student_records.csv")

#Whole dataframe
# print(df.mean(numeric_only=True)) #average
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count()) #count the total


#single dataframe
# print(df["StudentID"].mean())
# print(df["CGPA"].sum())
# print(df["CGPA"].min())
# print(df["CGPA"].max())
# print(df["CGPA"].count())

