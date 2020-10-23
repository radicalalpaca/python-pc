import requests
import problem18

url = "https://projecteuler.net/project/resources/p067_triangle.txt"


def scrape():
    r = requests.get(url).text
    triangle = []
    for row in r.split("\n"):
        triangle.append([int(i) for i in row.split(" ")])
        if len(triangle) == 100:
            return triangle


if __name__ == '__main__':
    print(problem18.path_sum(scrape()))
