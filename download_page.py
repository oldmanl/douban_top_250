import requests


def download_page(url):
    headers = {
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.117 Safari/537.36 '
    }
    proxies = {'http': 'http://127.0.0.1:1087', 'https': 'https://127.0.0.1:1087'}
    data = requests.get(url, headers=headers, proxies=proxies).content
    return data
