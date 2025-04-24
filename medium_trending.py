import feedparser
import requests
from langdetect import detect
import re

def is_spam(text):
    # Common spam indicators
    spam_indicators = [
        r'buy now',
        r'click here',
        r'limited time',
        r'act now',
        r'best price',
        r'cheap',
        r'discount',
        r'free trial',
        r'guaranteed',
        r'limited offer',
        r'make money',
        r'no cost',
        r'no obligation',
        r'no purchase',
        r'no risk',
        r'order now',
        r'please read',
        r'promise you',
        r'pure profit',
        r'risk-free',
        r'satisfaction guaranteed',
        r'save money',
        r'save big',
        r'save big money',
        r'special promotion'
    ]
    
    text_lower = text.lower()
    for indicator in spam_indicators:
        if re.search(indicator, text_lower):
            return True
    return False

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def get_top_tech_articles():
    feed_url = "https://medium.com/feed/tag/programming"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(feed_url, headers=headers)
    feed = feedparser.parse(response.content)
    
    valid_articles = []
    for entry in feed.entries:
        # Skip if content is not in English
        if not is_english(entry.title) or not is_english(entry.summary):
            continue
            
        # Skip if content appears to be spam
        if is_spam(entry.title) or is_spam(entry.summary):
            continue
            
        valid_articles.append({
            "title": entry.title,
            "link": entry.link,
            "content": entry.summary
        })
        
        # Stop after getting 5 valid articles
        if len(valid_articles) >= 5:
            break
            
    return valid_articles
