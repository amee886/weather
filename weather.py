import requests


def create_params():
    return {
        'nTqM': '',
        'lang': 'ru'
    }


def fetch_weather(location, params):
    response = requests.get(f"https://wttr.in/{location}", params=params)
    response.raise_for_status()
    return response.text


def print_weather(location):
    params = create_params()
    weather_info = fetch_weather(location, params)
    print(weather_info)


def get_weather(locations):
    for location in locations:
        print_weather(location)


if __name__ == "__main__":
    locations = ["London", "svo", "Череповец"]
    get_weather(locations)
