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
#import typer
from datetime import date

#app = typer.Typer()
parser = argparse.ArgumentParser(description='Create To-do Lists')
parser.add_argument('--d','--day', type=date, metavar='', required=True, help='a date for a task')
parser.add_argument('--t','--task', type=str, metavar='', required=True, help='a task to perform')
args = parser.parse_args()

# Verify if date_tasks exist
json_path = 'date_tasks.json'
if os.path.exists(json_path):
    with open('date_tasks.json', 'r') as f:
        date_tasks = json.loads(f.read())
        date_tasks = defaultdict(list, date_tasks)
        # IMPORTANT: this is how one opens up a debugger: `import pdb; pdb.set_trace()`.
else:
    date_tasks = defaultdict(list)

#@app.command()
def add_one_time_task(day, task):
    date_tasks[day].append(task)
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

#@app.command()
def add_weekly_task(day_of_the_week, task):
    date_tasks[day_of_the_week].append(task)
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

#@app.command()
def show_tasks(day):
    list_of_the_day = date_tasks[day]
    isoday = date.fromisoformat(day)
    if isoday.weekday() == 0:
        list_of_the_day.extend(date_tasks['Monday'])
    if isoday.weekday() == 1:
        list_of_the_day.extend(date_tasks['Tuesday'])
    if isoday.weekday() == 2:
        list_of_the_day.extend(date_tasks['Wednesday'])
    if isoday.weekday() == 3:
        list_of_the_day.extend(date_tasks['Thursday'])
    if isoday.weekday() == 4:
        list_of_the_day.extend(date_tasks['Friday'])
    if isoday.weekday() == 5:
        list_of_the_day.extend(date_tasks['Saturday'])
    if isoday.weekday() == 6:
        list_of_the_day.extend(date_tasks['Sunday'])
    print(list_of_the_day)

if __name__ == '__main__':
    list_of_the_day = show_tasks(args.day)