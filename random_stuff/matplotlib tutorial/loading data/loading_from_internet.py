import matplotlib.pyplot as plt
import numpy as np
import requests
import matplotlib.dates as mdates


def graph_data():
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = requests.get(stock_price_url).text
    split_source = source_code.split("\n")
    date = []
    closep = []

    for line in split_source[1:]:
        split_line = line.split(",")
        date.append(mdates.datestr2num(split_line[0]))
        closep.append(split_line[1])

    return date, closep


plt.plot_date(graph_data()[0], graph_data()[1], "-", label="Price")

plt.xlabel("date")
plt.ylabel("price")
plt.title("TSLA stock")
plt.legend()
plt.show()


