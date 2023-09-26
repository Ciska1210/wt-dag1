print("start csv read application")

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r,rij in df.iterrows():
    print(rij["Name"])