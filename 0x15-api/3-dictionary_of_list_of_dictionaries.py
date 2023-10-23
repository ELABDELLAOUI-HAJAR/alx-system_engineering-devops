#!/usr/bin/python3
"""script that, using this REST API,,
returns information about all Employees TODO list progress
then export the data in the JSON format
"""
import json
import re
import requests
from sys import argv


if __name__ == "__main__":
    API = "https://jsonplaceholder.typicode.com"
    users_dict = {}
    users_json = requests.get(f'{API}/users').json()
    users_id = [user.get("id") for user in users_json]

    for id in users_id:
        usr_json = requests.get(f'{API}/users/{id}').json()
        todos_json = requests.get(f'{API}/todos').json()

        user_name = usr_json.get('username')
        usr_todos = [task for task in todos_json if task.get('userId') == id]

        data = [{
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
                } for task in usr_todos
                ]
        users_dict[f'{id}'] = data

    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_dict, file)
