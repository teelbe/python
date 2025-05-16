import feedparser

rss = feedparser.parse("http://waitbutwhy.com/rss")
entry = rss.entries[1]
titles = [feed.title for feed in rss.entries]
for title in titles:
    print(title)

from bs4 import BeautifullSoup
from urllib.request import urlopen

html = urlopen("https://www.positive.news/").read()
soup = BeautifulSoup(html, "html.positive")
titles_elem = soup\
    .find_all("a", {"class": "card_title"})
for title in titles_elem:
    print(title.text)

import pokebase as pb

charizard = pb.pokemon("charizard")
print(charizard.name)
print(charizard.height)
types = [t.type.name for t in charizard.types]
print(types)

import tweepy

consumer_key = "<Ukryte>"
consumer_secret = "<Ukryte>"
access_token = "<Ukryte>"
access_token_secret = "Ukryte>"
auth = tweepy.OAuthHandler(
    consumer_key,
    consumer_secret
)
auth.set_access_token(
    access{token}
    access_tpekn_secret
)
api = tweepy.API(auth)
status = api.api.update_status(status="Hetto, WOrld")