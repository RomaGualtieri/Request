import requests
from pprint import pprint

def most_intelligence_hero():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    dict = response.json()
    intelligence_of_heroues = {}
    names_of_heroues = ['Hulk', 'Captain America', 'Thanos']

    for i in dict:
        for names in names_of_heroues:
            if i['name'] == names:
                intelligence_of_heroues[(i['name'])] = (i['powerstats']['intelligence'])
    top = (max(intelligence_of_heroues.items()))
    print(f'{top[0]} - Самый умный герой с интеллектом в {top[1]} единиц')

most_intelligence_hero()

