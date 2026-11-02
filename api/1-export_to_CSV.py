#!/usr/bin/python3
"""
Export an employee's TODO list to a CSV file named USER_ID.csv.

Usage: ./1-export_to_CSV.py EMPLOYEE_ID
"""
import csv
import json
import sys
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Return the decoded JSON body of a GET request to url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write the tasks of the employee ID given as argument to USER_ID.csv."""
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])
    user = fetch_json("{}/users/{}".format(BASE_URL, user_id))
    todos = fetch_json("{}/todos?userId={}".format(BASE_URL, user_id))

    username = user.get("username")
    file_name = "{}.csv".format(user_id)

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                             todo.get("title")])


if __name__ == "__main__":
    main()
