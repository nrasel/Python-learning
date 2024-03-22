import requests
import json

query=input("What type of news are you interested in? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-02-22&sortBy=publishedAt&apiKey=68a92cad467f42ccb20f9f1ebc697ef8"
r=requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------")