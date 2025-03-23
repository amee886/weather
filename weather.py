import requests

place_first= "London"
place_second = "svo"
place_third= "Череповец"
url_template="https://wttr.in/{}?nTqM&lang=ru"
url = url_template.format(place_third)
response=requests.get(url)
response.raise_for_status()
print(response.text)

