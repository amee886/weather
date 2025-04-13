import requests


def get_weather(locations):
    for location in locations:
        params = {
            'nTqM': '',
            'lang': 'ru'
        }
        response = requests.get(f"https://wttr.in/{location}", params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    locations = ["London", "svo", "Череповец"]
    get_weather(locations)  
