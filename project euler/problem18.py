import requests
from bs4 import BeautifulSoup

url = "https://projecteuler.net/problem=18"


def scrape():
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")


def path_sum():
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    


if __name__ == '__main__':
    print(path_sum())
