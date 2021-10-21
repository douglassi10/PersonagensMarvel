import requests
from time import time
import os
import hashlib



ts = int(time())
concatena = str(ts) + 'd53d63b665c1673193e9e5900b6424e821eafe54' + 'c349492697318809c3541cc551a49b0f'

my_hash = hashlib.md5(concatena.encode()).hexdigest()

parametros = {"nameStartsWith": 'Spider-Man', "ts": ts, "apikey": 'c349492697318809c3541cc551a49b0f', "hash": my_hash} 

r = requests.get('https://gateway.marvel.com:443/v1/public/characters', parametros)
print(r.url)
print(r.status_code)
print(r.encoding)
print(r.headers['date'])
print(r.headers['content-type'])
conteudo =  r.json()
personagens = conteudo['data']['results']
for p in personagens:
    print(p['name'])
    print(p['description'])


