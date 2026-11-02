#!/usr/bin/python3
"""
Export an employee's TODO list to a JSON file named USER_ID.json.

Usage: ./2-export_to_JSON.py EMPLOYEE_ID
"""
import json
import sys
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Return the decoded JSON body of a GET request to url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write the tasks of the employee ID given as argument to USER_ID.json."""
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])
    user = fetch_json("{}/users/{}".format(BASE_URL, user_id))
    todos = fetch_json("{}/todos?userId={}".format(BASE_URL, user_id))

    username = user.get("username")
    tasks = [{"task": todo.get("title"),
              "completed": todo.get("completed"),
              "username": username} for todo in todos]

    file_name = "{}.json".format(user_id)
    with open(file_name, "w") as json_file:
        json.dump({str(user_id): tasks}, json_file)


if __name__ == "__main__":
    main()
