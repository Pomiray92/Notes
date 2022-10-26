
dict = {
    "next": "a link",
    "results": [
        {"name": "a", "items": ["Shaban"]},
        {"name": "b", "items": ["Peer"]},
        {"name": "c", "items": ["Jacques"]},
        {"name": "d", "items": ["Muhannad"]}
    ]
}

# for r in dict["results"]:
#     print(r["name"])

# print(dict["results"][0]["items"][0])
    
# for r in dict["results"]:
#     print(r["items"][0])
    
# print(dict["results"][0]["items"][0])

# crate a file with names, A, B, C,and D from the dict

# file = open("pokemon.txt", "a")
# for result in dict["results"]:
#     file.write(f"{result['name']}\n")
# file.close()

# pokemon.txt

# Interacting with an API(Application programming interface)

import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'

response = requests.get(BASE_URL)

data = response.json()
# print(data.json())

# for result in data["results"]:
#     print(result["name"])
    


def fetch_pokemons(url):
    
    response = requests.get(url)
    data = response.json()
    file = open("pokemon.txt", "a")
    
    for result in data["results"]:
        file.write(f"{result['name']}\n")
    file.close()
    
    # next_url = data["next"]
    # print(next_url)
    
    print(data.get("next", " "))
    
    if data.get("next", None):
        fetch_pokemons(data.get("next"))

fetch_pokemons(BASE_URL)

# JSON -> Javascript Object Notation -> 


















