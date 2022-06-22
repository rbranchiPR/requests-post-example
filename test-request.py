import requests

json = {
    'name': 'Reinaldo'
}

headers = {
    'Content-type': 'application/json'
}

peticion = requests.post('http://localhost:5000/', headers = headers, json = json)

print(peticion.content)