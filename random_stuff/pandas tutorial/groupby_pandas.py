import pandas as pd

df = pd.read_csv("data/Minimum Wage Data.csv")

gb = df.groupby("State")
#gb.get_group("Alabama").set_index("Year").head()

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

print(act_min_wage.head())


