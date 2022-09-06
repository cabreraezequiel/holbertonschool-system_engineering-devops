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
    r = requests.get("https://jsonplaceholder.typicode.com/todos".format
                     (sys.argv[1]))

    with open("{}.csv".format(user_id), 'w') as f:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED",
                      "TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
#        writer = csv.writer(f)
        for i in r.json():
            if i.get("userId") == user_id:
                writer.writerow({"USER_ID": str(user_id),
                                 "USERNAME": user_username,
                                 "TASK_COMPLETED": str(i.get("completed")),
                                 "TASK_TITLE": i.get("title")})
#               writer.writerow([str(user_id), user_username,
# str(i.get("completed")), i.get("title")])
