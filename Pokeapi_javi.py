import requests
from pprint import pp
import json

pokemon = input("Decime el nombre de un pokemon ")

url = "https://pokeapi.co/api/v2/pokemon/"+pokemon+"/?limit=10000&offset=0" #Solicito la informacion de TODOS los pokemones
response = requests.get(url)

if response.status_code != 200:
    print("Ese pokemon no existe")

response.json()
json_data = json.loads(str(response.content, encoding='utf-8')) #Convierto las cosas en un JSON, aca convierto las cosas a un string pq es lo que toma el json 

ability_list = []

for i in range(0,len(json_data['abilities'])):
    ability = ((json_data['abilities'])[i])['ability']['name']
    ability_list.append(ability)
    
dict_total={'pokemon': pokemon,
'Id': json_data['id'],
'Ability': ability_list}

print(dict_total)




