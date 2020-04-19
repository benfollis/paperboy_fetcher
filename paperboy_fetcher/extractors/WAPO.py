"""
As of Mid April 2020, the code below will extract the article text from
Note, WAPO is really stingy about giving us true data, so we probably
will break soon.
"""
from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.find(attrs={'class': 'article-body'})
    content = []
    content_nodes = body.find_all('p')
    for node in content_nodes:
        for chunk in node.strings:
            content.append(chunk)
    article = ' '.join(content)
    return {
        'title': title,
        'article': article
    }