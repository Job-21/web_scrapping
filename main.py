from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com")
data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup.title.string)
article_tag = soup.find_all(name="a", class_="titlelink")
article_text = [text.getText() for text in article_tag]
url = [url_text.get("href") for url_text in article_tag]

votes = soup.find_all(name="span", class_="score")
upvotes = [int(vote.getText().split()[0]) for vote in votes]
print(url)
print(article_text)
print(upvotes)
print(len(upvotes))
# index = upvotes.index(max(upvotes))
highest = max(upvotes)
indext = upvotes.index(highest)
print(indext)

print(f"ARTICLE IS : {article_text[indext]} and the URL IS : {url[indext]}")



# print(url)
# print(article_tag.getText())
#
# vote = soup.find(name="span", class_="score", id="score_32715437")
# print(f"The upvote is {vote.getText()}")

# with open("index.html") as file:
#     content = file.read()
#
# data = BeautifulSoup(content, "html.parser")
# # print(data.title.string)
# # print(data.ul)
# anchors = data.find_all(name="a")
# print(anchors[0].string)
#
# img = data.select(selector=".second-card .notice-container .notice-logo img")
# print(img)
# for tag in img:
#     url = tag.get("src")
# print(url)
#
# stripe = data.find(name="div", class_="black-stripe")
# print(stripe.get_text())
