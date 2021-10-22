import requests
from time import time
import os
import hashlib

ts = int(time())
concatena = str(ts) + 'd53d63b665c1673193e9e5900b6424e821eafe54' + 'c349492697318809c3541cc551a49b0f'

my_hash = hashlib.md5(concatena.encode()).hexdigest()

print('Spider-Man')
print('Captain America')
print('Black Widow')
print('Iron Man')
print('Hulk')
print('Deadpool\n')
op = input('Digite o nome do seu personagem favorito.\n')
print('página html atualizada.')
    


parametros = {"nameStartsWith": op, "ts": ts, "apikey": 'c349492697318809c3541cc551a49b0f', "hash": my_hash} 

r = requests.get('https://gateway.marvel.com:443/v1/public/characters', parametros)
#r = requests.get('https://gateway.marvel.com:443/v1/public/stories/1/characters', parametros)
#print(r.url)
print(r.status_code)
print(r.encoding)
print(r.headers['date'])
print(r.headers['content-type'])
conteudo =  r.json()
personagens = conteudo['data']['results']
for p in personagens:
    print(p['name'])

pagina = open('personagens.html', 'w')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8"/>
<title>Personagens Marvel</title>
</head>
<body><div align='center'>""")
for p in personagens:
    a = p['thumbnail']['path'] + '.jpg'
    pagina.write("<img src='%s' width='200px'> </img>\n" % a) 
    pagina.write("<h3>%s</h3>\n" % p['name'])
    pagina.write("<p>%s</p>\n" % p['description'])
    
    
pagina.write("""</></body>
</html> 
""")
pagina.close()

