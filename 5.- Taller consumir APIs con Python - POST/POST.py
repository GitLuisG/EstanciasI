import requests
import json

url='https://httpbin.org/post'
payload={'nombre':'Luis', 'Curso':'python', 'Nivel':'Intermedio'}
#el metodo post crea un recurso dentro del servidor mientras que GET lo obtenia del servidor
response = requests.post(url, data=json.dumps(payload))
#Json post se encarga deserializarlos
print(response.content)
