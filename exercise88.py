import pandas as pd

df = pd.read_csv('countries_by_area.txt')
df["density"] = df["population_2013"] / df["area_sqkm"]
# df["density"] = [i/j for i, j in zip(df["population_2013"], df["area_sqkm"])]

df = df.sort_values("density", ascending=False)
print(df.head()['country'].to_string(index=False))
