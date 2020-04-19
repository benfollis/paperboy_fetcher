"""
As of Mid April 2020, the code below will extract the article text from BBCs news articles. It will not remove the
Word Have Your say subsection, but hopefully that won't prevent usage of the data.
"""
from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.find(attrs={'property': 'articleBody'})
    if body is None:
        raise Exception("Unable to parse")
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