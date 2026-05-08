import pandas as pd
#importing csv files
df = pd.read_csv("student_records.csv" )

print(df)
# print(df.head())
print(df.to_string())


df_json = pd.read_json("")
print(df_json.to_string())  #to print all data