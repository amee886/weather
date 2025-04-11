import requests


locations = ["London", "svo", "Череповец"]


for i in locations:
    params = {
        'nTqM': '',
        'lang': 'ru'
    }
    response = requests.get(f"https://wttr.in/{i}",params=params)
    response.raise_for_status()
    print(response.text)
