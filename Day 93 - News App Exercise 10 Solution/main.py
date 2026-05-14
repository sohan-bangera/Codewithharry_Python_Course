import requests
import json
query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-04-14&sortBy=publishedAt&apiKey=50ccd84e320e4c948e2b8fe7ad6dbaff"
r = requests.get(url)

news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print("Title: ", article["title"])
    print(article["description"])
    print("-------------------------------------")
# api key = 50ccd84e320e4c948e2b8fe7ad6dbaff