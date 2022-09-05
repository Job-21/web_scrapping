from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.find(name="h1").getText()
title = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

print(page_title)
movie_list = title[::-1]
with open("greatest_movies.txt", "w", encoding="utf-8") as movies:
    movies.write(page_title)
    for item in movie_list:
        movies.write("\n")
        movies.write(item)
        movies.write("\n")
