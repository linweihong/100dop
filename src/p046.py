# Music time machine


import sys

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

from constants import SPOTIFY_ID, SPOTIFY_TOKEN


def billboard_url(d: str) -> str:
    "Generate a URL for a time period, given user input."
    return f"https://billboard.com/charts/hot-100/{d}"


year = input("Which year do you want to travel to? Type the date in 'YYYY-MM-DD': ")
url = billboard_url(year)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_TOKEN,
        redirect_uri="https://example.com/",
        scope="playlist-modify-private",
    )
)

r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
with open("./src/p046_test.txt", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
song_names = [name.text.strip() for name in soup.select("li ul li h3.c-title")]
artist_names = [
    name.text.strip() for name in soup.select("li ul li span.c-label.a-no-trucate")
]
tracklist = [
    {"artist": artist, "track": track}
    for artist, track in zip(artist_names, song_names)
]

for listing in tracklist:
    sys.stdout.write(f"\rChecking {listing['track']} ...".ljust(88, " "))
    sys.stdout.flush()
    results = sp.search(
        q=listing["track"],
        type="track",
        limit=1,
        market="US",
    )
    try:
        artist = results["tracks"]["items"][0]["artists"][0]["name"]
        track = results["tracks"]["items"][0]["name"]
        uri = results["tracks"]["items"][0]["uri"]
    except KeyError:
        print(f"{listing['track']} not found.")
    else:
        listing["uri"] = uri

pl = sp.user_playlist_create(
    user=sp.me()["id"],
    name=f"{year} Billboard 100",
    public=False,
)

sp.user_playlist_add_tracks(
    user=sp.me()["id"],
    playlist_id=pl["id"],
    tracks=[track.get("uri") for track in tracklist if track.get("uri")],
)
