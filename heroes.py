import requests


def superheroes(names: list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    full_list = response.json()
    smart_list = sorted([[_['powerstats']['intelligence'], _['name']] for _ in full_list if _['name'] in names])
    smart = f'Самый умный герой: {smart_list[-1][1]}'
    return smart
