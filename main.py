#!/usr/bin/env python
# coding: utf-8

# To-do-list Project

# Goal:
# To create a tool to organize daily, weekly, and monthly activities

# Dates on iso format: 'YYYY-MM-DD'
# Names of the week: Monday, Tuesday…

# Import modules
import pandas as pd
import numpy as np
import sys
import os.path
import argparse
import simplejson as json
from collections import defaultdict
from datetime import date

# Verify if date_tasks exist
json_path = 'date_tasks.json'
if os.path.exists(json_path):
    with open('date_tasks.json', 'r') as f:
        date_tasks = json.loads(f.read())
        date_tasks = defaultdict(list, date_tasks)
        # IMPORTANT: this is how one opens up a debugger: `import pdb; pdb.set_trace()`.
else:
    date_tasks = defaultdict(list)

def main(a):
    date_tasks[a.DATE.isoformat()].append(a.t)
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)
    print(a.t + " added to " + a.DATE.isoformat() + " list!")

days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def show_tasks(a):
    list_of_the_day = date_tasks[a.DATE.isoformat()]
    for n in range(7):
        if a.DATE.weekday() == n:
            list_of_the_day.extend(date_tasks[days_of_the_week[n]])
    print(list_of_the_day)

def add_weekly_task(a):
    for i in a.wd:
        date_tasks[i].append(a.t)
        print(a.t + " added to " + i + " list!")
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create To-do Lists')
    parser.add_argument(
        'DATE', 
        type=date.fromisoformat, 
        help='a date for a task'
    )
    parser.add_argument(
        '-t', 
        type=str,
        help='a task to perform'
    )
    parser.add_argument(
        '-wd', 
        type=str, 
        choices=days_of_the_week.values(),
        nargs="*",
        help='a day of the week'
    )

    args = parser.parse_args()
    if args.t is None:
        show_tasks(args)
    elif args.wd is not None:
        add_weekly_task(args)
    else:
        main(args)
