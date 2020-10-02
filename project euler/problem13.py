import time
import requests
from bs4 import BeautifulSoup

url = "https://projecteuler.net/problem=13"

def scrape():
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    problem_content = str(list(soup.find(class_="problem_content"))[3])
    content = problem_content[74:].split("\n")
    numbers = []
    for number in content:
        numbers.append(number[:50])
    return numbers

def sum():
    sum = 0
    for number in scrape():
        sum += int(number)
    print(str(sum)[:10])


if __name__ == '__main__':
    scrape()
    sum()
