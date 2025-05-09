![Static Badge](https://img.shields.io/badge/python-3.13.0-brightgreen)
![Static Badge](https://img.shields.io/badge/requests-2.32.3-brightgreen)

# Weather Fetcher
Этот скрипт позволяет получать текущую погоду для заданных местоположений с помощью API сервиса [wttr.in](https://wttr.in).

## Описание

Скрипт отправляет GET-запросы к API wttr.in для получения информации о погоде в указанных городах. Поддерживаются как английские, так и русские названия мест.

## Установка

Для работы скрипта необходимо установить файл requirements.txt. Вы можете сделать это с помощью pip:

```bash
python -m pip install -r requirements.txt
```
## Использование

1. Скопируйте код в файл, например, weather.py.
2. Измените список locations, добавив необходимые вам города.
3. Запустите скрипт:

```bash
python weather.py
```
## Пример

В locations можно указать любые города, например:

```python
locations = ["London", "svo", "Череповец"]
```
Скрипт выведет текущую погоду для каждого из указанных местоположений.
