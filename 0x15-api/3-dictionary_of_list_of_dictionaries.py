#!/usr/bin/python3
"""using a REST API, for a given employee ID, and exports in json format"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    user_id_name = {}
    for i in r.json():
        user_id_name[str(i.get("id"))] = i.get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos")

    with open("todo_all_employees.json", 'a') as f:
        users = {}
        for k, v in user_id_name.items():
            user_dict_list = []
            for i in r.json():
                if str(i.get("userId")) == str(k):
                    user_dict = {'username': v,
                                 'task': i.get("title"),
                                 'completed': str(i.get("completed"))}
                    user_dict_list.append(user_dict)
                users.update({k: user_dict_list})
        json.dump(users, f)
