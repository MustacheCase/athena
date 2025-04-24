from dotenv import load_dotenv  # added to load .env values
load_dotenv()  # load environment variables from .env

from medium_trending import get_top_tech_articles
from summarizer import summarize_article
from extract_content import extract_article
from telegram import send_to_telegram
import sys

def main():
    articles = get_top_tech_articles()
    for i, article in enumerate(articles, 1):
        title = article["title"]
        url = article["link"]
        content = article["content"]  # MediumAPI might have limits
        content = extract_article(url)[1]
        summary = summarize_article(title, content)
        
        # Improved print output
        print(f"Article {i}: {title}")
        print(f"Link: {url}\n")
        print(f"Summary: \n")
        print(summary)
        print("\n" + "=" * 50 + "\n")
        sys.stdout.flush()  # Ensure output is flushed immediately
        
        # Send to Telegram
        telegram_message = f"📰 *{title}*\n\n🔗 {url}\n\n📝 *Summary:*\n{summary}"
        try:
            send_to_telegram(telegram_message)
            print(f"✅ Article {i} sent to Telegram successfully")
        except Exception as e:
            print(f"❌ Failed to send article {i} to Telegram: {str(e)}")
    
if __name__ == "__main__":
    main()