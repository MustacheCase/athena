import feedparser
import requests

def get_top_tech_articles():
    feed_url = "https://medium.com/feed/tag/programming"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(feed_url, headers=headers)
    feed = feedparser.parse(response.content)
    return [
        {
            "title": entry.title,
            "link": entry.link,
            "content": entry.summary
        }
        for entry in feed.entries[:5]
    ]
