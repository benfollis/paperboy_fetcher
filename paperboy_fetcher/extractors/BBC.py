from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.find(attrs={'property': 'articleBody'})
    content = []
    content_nodes = body.find_all('p')
    for node in content_nodes:
        content.append(node.string)
    return ' '.join(content)
