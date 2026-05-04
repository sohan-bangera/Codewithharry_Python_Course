import requests
from bs4 import BeautifulSoup
# response = requests.get("https://www.google.com")
# print(response.text)




url = "https://www.google.com"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for heading in soup.find_all("a"):
    print(heading.text)


# data = {
#     "title":'foo',
#     "body":'bar',
#     "userId":1,
# }

# header = {
#     'Content-type': 'application/json; charset=UTF-8',
# }

# response = requests.post(url, headers=header, json=data)
# print(response.text)