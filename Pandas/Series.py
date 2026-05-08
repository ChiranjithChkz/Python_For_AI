import pandas as pd


#integer
# data = [100, 102, 103]
# series = pd.Series(data)
# print(series)


#float
data = [100.2, 102.3, 103.4]
series = pd.Series(data)
print(series)


#character
data = ["A", "B", "C"]
series = pd.Series(data)
print(series)


data = [102.3, 103.2, 109.5]
series = pd.Series(data, index=["a", "b", "c"])
print(series)

#access value with index
data = [102.3, 103.2, 109.5]
series = pd.Series(data, index=["a", "b", "c"])
print(series.loc["c"])
#print(series.iloc[indexNUmber])


calories = {"Day 1": 1750, "Day 2": 2100, "Day-3": 1700}
series = pd.Series(calories)
print(series)  


#update series
calories = {"Day 1": 1750, "Day 2": 2100, "Day-3": 1700}
series = pd.Series(calories)
series.loc["Day-3"] += 500
print(series)  


#practice 
section = {1: "Bulbasaur", 2: "Lvysaur", 3: "Venusaur", 3: "Charmander", 4: "Charmeleon", 5: "Charizard"}

series = pd.Series(section)
print(series)



