#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
then export the data in the JSON format
"""
import json
import re
import requests
from sys import argv


if __name__ == "__main__":
    API = "https://jsonplaceholder.typicode.com"
    if re.fullmatch(r'\d+', argv[1]):
        id = int(argv[1])

        usr_json = requests.get(f'{API}/users/{id}').json()
        todos_json = requests.get(f'{API}/todos').json()

        user_name = usr_json.get('username')
        usr_todos = [task for task in todos_json if task.get('userId') == id]

        with open(f'{id}.json', 'w') as file:
            data = [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_name
                    } for task in usr_todos
                    ]
            user_data = {f'{id}': data}
            json.dump(user_data, file)
