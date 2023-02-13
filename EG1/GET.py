import requests
import json


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "delectus aut autem", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()
response.status_code