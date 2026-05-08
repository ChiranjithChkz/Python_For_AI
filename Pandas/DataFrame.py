import pandas as pd

#dataFrame = A tabular data structure with rows and columns: (2 Dimensional)
#            Similar to an Excel spreadsheet


data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])


print(df)
print(df.loc["Employee 3"])
print(df.iloc[0])

#Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]


#Add a new row 
# new_row = pd.DataFrame([{"Name" : "Sandy", "Age" : 28, "Job" : "Engineer"}], index=["Employee 4"])

#add new rows
new_rows = pd.DataFrame([{"Name" : "Sandy", "Age" : 28, "Job" : "Engineer"}, {"Name" : "John Wick", "Age" : 60, "Job" : "Killer"}], index=["Employee 4", "Employee 5"])


df = pd.concat([df, new_rows])

print(df)