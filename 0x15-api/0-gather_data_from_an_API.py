#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
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

        user_name = usr_json.get('name')
        usr_todos = [task for task in todos_json if task.get('userId') == id]
        todos_done = [task for task in usr_todos if task.get('completed')]

        print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                              len(todos_done),
                                                              len(usr_todos)
                                                              )
              )

        for task in todos_done:
            print('\t {}'.format(task.get('title')))
