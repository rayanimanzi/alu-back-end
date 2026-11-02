# alu-back-end

Python scripts that gather employee TODO data from a REST API and export it to CSV and JSON.

## Project layout

- `api/0-gather_data_from_an_API.py`: prints one employee's TODO progress and the titles of completed tasks.
- `api/1-export_to_CSV.py`: exports one employee's tasks to `USER_ID.csv`. (Planned)
- `api/2-export_to_JSON.py`: exports one employee's tasks to `USER_ID.json`. (Planned)
- `api/3-dictionary_of_list_of_dictionaries.py`: exports all employees' tasks to `todo_all_employees.json`. (Planned)

## Requirements

- Python 3.4.3 on Ubuntu 14.04 (`#!/usr/bin/python3`)
- Standard library only (`urllib`, `json`, `sys`, `csv`)
- PEP 8 style

## Usage

```bash
chmod +x api/0-gather_data_from_an_API.py
./api/0-gather_data_from_an_API.py 2
```

Example output for employee `2`:

```
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 ...
```

## Data source

[JSONPlaceholder](https://jsonplaceholder.typicode.com): `/users/{id}` and `/todos?userId={id}`.
