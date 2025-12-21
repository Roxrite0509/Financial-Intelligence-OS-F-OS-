import feedparser


def get_news(query: str):
    feed = feedparser.parse(
        f"https://news.google.com/rss/search?q={query}+bank"
    )
    return [e.title for e in feed.entries[:5]]
