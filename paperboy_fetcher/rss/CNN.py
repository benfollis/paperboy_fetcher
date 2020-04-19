"""
Parser for CNN rss, which we have to filter for articles
that only end in index.html. Articles other than that, use
different formats and we can't extract them (yet)
"""
from paperboy_fetcher.rss.nice_parser import extract_articles as base_extract

def extract_articles(url):
    candidates = base_extract(url)
    extracted = [article for article in candidates if article['link'].endswith('index.html')]
    return extracted
