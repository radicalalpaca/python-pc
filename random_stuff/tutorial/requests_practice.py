import requests

def google_search(query, num):
    r = requests.get("https://google.com/search",
                     params={"q": query, "num": num})
    return r.url

print(google_search("python", 1))