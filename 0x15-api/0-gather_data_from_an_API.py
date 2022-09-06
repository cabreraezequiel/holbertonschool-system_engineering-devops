#!/usr/bin/python3
"""using a REST API, for a given employee ID, returns information about
his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                     (sys.argv[1]))
    user_id = r.json().get("id")
    user_name = r.json().get("name")
    r = requests.get("https://jsonplaceholder.typicode.com/todos".format
                     (sys.argv[1]))
    tasks = 0
    fin_tasks = 0
    for i in r.json():
        if i.get("userId") == user_id and i.get("completed") is True:
            fin_tasks += 1
        if i.get("userId") == user_id:
            tasks += 1
    print("Employee {} is done with tasks({}/{})".format(user_name,
                                                         fin_tasks, tasks))
    for i in r.json():
        if i.get("userId") == user_id and i.get("completed") is True:
            print("\t {}".format(i.get("title")))
