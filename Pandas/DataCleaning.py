import pandas as pd

#Data cleaning = the process of fixing / removing:
#                incomplete, incorrect, or irrelevent data.
#                ~75% of work done with Pandas is data cleaning

df = pd.read_csv("student_records.csv")

#1. Drop irrelevent columns
# df = df.drop(columns=["CGPA", "StudentID"])

#2. Handle missing data
#dropna -> drop not available
# df = df.dropna(subset=[""])

#3.replace missing value
#fillna -> fill not available
#df = df.fillna({"Type2": "None"})

#3. Fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})


#4. Standardize text
#df["Name"] = df["Name"].str.lower()

#5.Fix data Types
#df["Name"] = df["Name"].astype(bool)

print(df)