"""
As of Mid April 2020, the code below will extract the article text from CNN news articles.
"""
from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.find(attrs={'itemprop': 'articleBody'})
    content = []
    content_nodes = body.find_all('div', attrs={'class': 'zn-body__paragraph'})
    for node in content_nodes:
        for chunk in node.strings:
            content.append(chunk)
    article = ' '.join(content)
    return {
        'title': title,
        'article': article
    }