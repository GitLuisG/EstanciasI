import requests
import json

url='https://httpbin.org/get?nombre=Luis&curse=python'
#args es un diccionario para el comando params
args={'nombre':'Luis', 'Curso':'python', 'Nivel':'Intermedio'}
response = requests.get(url, params=args)

#response_json = response.json()#Diccionario
#origin=response_json['origin']
#print(origin)

response_json= json.loads(response.text)
origin=response_json['origin']
print(origin)