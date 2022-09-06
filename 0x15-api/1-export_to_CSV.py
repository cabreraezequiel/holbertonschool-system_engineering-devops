#!/usr/bin/python3
"""using a REST API, for a given employee ID, returns information about
his/her TODO list progress"""
import csv
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                     (sys.argv[1]))
    user_id = r.json().get("id")
    user_username = r.json().get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos")

    with open("{}.csv".format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in r.json():
            if i.get("userId") == user_id:
                writer.writerow([str(user_id), user_username,
                                str(i.get("completed")), i.get("title")])
