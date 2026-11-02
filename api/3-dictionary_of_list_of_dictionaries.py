#!/usr/bin/python3
"""
Export the TODO lists of all employees to todo_all_employees.json.

Usage: ./3-dictionary_of_list_of_dictionaries.py
"""
import json
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Return the decoded JSON body of a GET request to url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write every employee's tasks to todo_all_employees.json."""
    users = fetch_json("{}/users".format(BASE_URL))
    todos = fetch_json("{}/todos".format(BASE_URL))

    usernames = {user.get("id"): user.get("username") for user in users}

    all_tasks = {}
    for todo in todos:
        user_id = todo.get("userId")
        entry = {"username": usernames.get(user_id),
                 "task": todo.get("title"),
                 "completed": todo.get("completed")}
        all_tasks.setdefault(str(user_id), []).append(entry)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
