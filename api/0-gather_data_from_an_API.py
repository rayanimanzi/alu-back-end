#!/usr/bin/python3
"""
Gather an employee's TODO list progress from a REST API.

Usage: ./0-gather_data_from_an_API.py EMPLOYEE_ID
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
    """Print the TODO progress for the employee ID given as argument."""
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user = fetch_json("{}/users/{}".format(BASE_URL, employee_id))
    todos = fetch_json("{}/todos?userId={}".format(BASE_URL, employee_id))

    employee_name = user.get("name")
    done = [todo for todo in todos if todo.get("completed")]
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done), total))
    for todo in done:
        print("\t {}".format(todo.get("title")))


if __name__ == "__main__":
    main()
