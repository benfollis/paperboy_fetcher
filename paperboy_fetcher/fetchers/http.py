"""
Useful for nice sources that don't do stupid things to prevent getting the data
WAPO is not one of these, so beware timeouts etc
"""

import urllib3
http = urllib3.PoolManager()

def fetch(url):
    response = http.request('GET', url)
    if (response.status != 200):
        raise ('Failed to fetch ' + url)
    return response.data