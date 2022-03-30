#!/usr/bin/env python
# coding: utf-8

# To-do-list Project

# Goal:
# To create a tool to organize daily, weekly, and monthly activities

# Dates on iso format: 'YYYY-MM-DD'
# Names of the week: Monday, Tuesday…

# Import modules
from re import A
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
    date_tasks[a.d.isoformat()].append(a.t)
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)
    print(a.t + " added to " + a.d.isoformat() + " list!")

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
    list_of_the_day = date_tasks[a.d.isoformat()]
    for n in range(7):
        if a.d.weekday() == n:
            list_of_the_day.extend(date_tasks[days_of_the_week[n]])
    print(list_of_the_day)

def add_weekly_task(a):
    for i in a.wd:
        date_tasks[i].append(a.t)
        print(a.t + " added to " + i + " list!")
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

def remove_task(a):
    date_tasks[a.d.isoformat()].remove(a.t)
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)
    print(a.t + " removed from " + a.d.isoformat() + " list!")

def remove_weekly_task(a):
    for i in a.wd:
        date_tasks[i].remove(a.t)
        print(a.t + " removed from " + i + " list!")
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

def remove_day_tasks(a):
    del date_tasks[a.d.isoformat()]
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)
    print("All tasks removed from "+a.d.isoformat()+" list!")

def empty_all():
    date_tasks.clear()
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)
    print("All tasks were deleted.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create To-do Lists')
    parser.add_argument(
        '-d', 
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
        help='one or more days of the week'
    )
    parser.add_argument(
        '-r',
        action='store_true',
        help='remove a task'
    )
    parser.add_argument(
        '-empty',
        action='store_true',
        help='empty all lists'
    )

    args = parser.parse_args()
    if args.empty:
        empty_all()
    elif args.r:
        if args.wd:
            remove_weekly_task(args)
        elif args.t:
            remove_task(args)
        else:
            remove_day_tasks(args)
    elif args.wd:
        add_weekly_task(args)
    elif args.t:
        main(args)
    else:
        show_tasks(args)

    # if args.t is None:
    #     show_tasks(args)
    # elif args.r == True:
    #     if args.t is None:
    #         remove_day_tasks(args)
    #     if args.wd is None:
    #         remove_task(args)
    #     else:
    #         remove_weekly_task(args)
    # elif args.wd is not None:
    #     add_weekly_task(args)
    # else:
    #     main(args)
    # print(args)
