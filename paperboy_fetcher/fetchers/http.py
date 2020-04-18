import urllib3
http = urllib3.PoolManager()


def fetch(url):
    response = http.request('GET', url)
    if (response.status != 200):
        raise ('Failed to fetch ' + url)
    return response.data