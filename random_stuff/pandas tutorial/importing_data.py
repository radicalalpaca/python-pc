import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/avocado.csv")
df = df.copy()[df["type"] == "organic"]
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date", ascending=True, inplace=True)

albany_df = df.copy()[df["region"] == "Albany"].set_index("Date")
albany_df.sort_index(inplace=True)
albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()

graph_df = pd.DataFrame()

for region in df["region"].unique():
    region_df = df.copy()[df["region"] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.plot(legend=False)
plt.show()