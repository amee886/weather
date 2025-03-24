import requests


place = ["London", "svo", "Череповец"]


for i in place:
    url_template = "https://wttr.in/"
    url_first = url_template.format(i)
    params = {
        'nTqM': '',
        'lang': 'ru'
    }
    response = requests.get(url_template + i, params=params)
    response.raise_for_status()
    print(response.text)
