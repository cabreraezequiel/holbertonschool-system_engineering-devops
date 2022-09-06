#!/usr/bin/python3
"""using a REST API, for a given employee ID, and exports in json format"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                     (sys.argv[1]))
    user_id = r.json().get("id")
    user_username = r.json().get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId=\
{}".format(sys.argv[1]))

    with open("{}.json".format(user_id), 'a') as f:
        user_dict_list = []
        for i in r.json():
            user_dict = {'task': i.get("title"),
                         'completed': str(i.get("completed")),
                         'username': user_username}
            user_dict_list += [user_dict]
        json.dump({user_id: user_dict_list}, f)
