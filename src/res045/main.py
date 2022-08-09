from importlib.resources import contents
from inspect import classify_class_attrs

import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
movie_names = [
    movie.get("alt") for movie in soup.find_all(name="img", class_="jsx-952983560")
]
print(movie_names)
with open("./src/res045/movies.txt", "w", encoding="utf-8") as f:
    f.write(
        "\n".join(f"{i:03}) {name}" for i, name in zip(range(1, 101), movie_names[1:]))
    )
