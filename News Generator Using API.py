import requests
import json

query = input('News type : ')
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-06&sortBy=publishedAt&apiKey=9603632f6f9148a5840ec54200b8f2df"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print('________________________________________________________')
