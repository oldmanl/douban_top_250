import requests


def download_page(url):
    headers = {
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.117 Safari/537.36 '
    }
    data = requests.get(url, headers=headers).content
    return data
