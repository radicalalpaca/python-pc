import requests
from bs4 import BeautifulSoup

url = "https://projecteuler.net/problem=18"


def scrape():
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    triangle = []
    for line in soup.find_all(class_="monospace center", limit=3)[-1].stripped_strings:
        triangle.append([int(i) for i in line.split(" ")])
    return triangle


def path_sum(triangle):
    triangle.reverse()
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i]) - 1):
            triangle[i + 1][j] += max([triangle[i][j], triangle[i][j + 1]])
    return triangle[-1]


if __name__ == '__main__':
    print(path_sum(scrape()))
