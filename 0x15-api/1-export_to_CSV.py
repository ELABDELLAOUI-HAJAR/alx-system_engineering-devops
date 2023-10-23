#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
then export the data in the CSV format
"""
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

        with open(f'{id}.csv', 'w') as file:
            for task in usr_todos:
                task_status = task.get('completed')
                task_title = task.get('title')
                file.write('"{}","{}","{}","{}"\n'.format(
                                                        id,
                                                        user_name,
                                                        task_status,
                                                        task_title
                                                        )
                           )
