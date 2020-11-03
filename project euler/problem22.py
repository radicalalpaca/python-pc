import requests
from bs4 import BeautifulSoup


def scrape(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    names = soup.string.split('","')
    names[0] = "MARY"
    names[-1] = "ALONSO"
    return names


def values(name):
    characters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    value = 0
    for letter in name:
        for i in range(len(characters)):
            if letter == characters[i]:
                value += i + 1
    return value


if __name__ == '__main__':
    name_list = scrape("https://projecteuler.net/project/resources/p022_names.txt")
    name_list.sort()
    total = 0
    for j in range(len(name_list)):
        total += values(name_list[j]) * (j + 1)
    print(total)
