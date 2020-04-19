"""
Base Parser for feeds that give us well formatted rss
"""
import feedparser


def extract_articles(url):
    feed = feedparser.parse(url)
    return feed['items']
