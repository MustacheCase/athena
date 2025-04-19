import sys
import requests
from bs4 import BeautifulSoup
from summarizer import summarize_article

def extract_article(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try to extract the title
    title = soup.title.string if soup.title else 'Untitled'
    
    # Extract all paragraph texts
    paragraphs = soup.find_all('p')
    content = "\n\n".join(p.get_text() for p in paragraphs if p.get_text().strip())
    
    return title, content

def process_article(url):
    # Extract article content and generate the summary
    title, content = extract_article(url)
    return summarize_article(title, content)