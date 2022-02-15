#!/usr/bin/env python
# coding: utf-8

# # To-do-list Project
# 
# ## Goal:
# To create a tool to organize daily, weekly, and monthly activities

# Import modules
import pandas as pd
import numpy as np
import sys
import os.path
import simplejson as json
from collections import defaultdict
import typer

app = typer.Typer()

# Verify if date_taks exist
# if os.path.exists('date_taks.json'): # True or False
json_path = 'date_tasks.json'
if os.path.exists(json_path):
    with open('date_tasks.json', 'r') as f:
        date_tasks = json.loads(f.read())
        # TODO: how to transform dict -> defaultdict.
        date_tasks = defaultdict(list, date_tasks)
        # IMPORTANT: this is how one opens up a debugger: `import pdb; pdb.set_trace()`.
else:
    date_tasks = defaultdict(list)

@app.command()
def add_one_time_task(day, task):
    date_tasks[day].append(task)
    print(date_tasks[day])
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

@app.command()
def show_taks(day):
    print(date_tasks[day])

if __name__ == '__main__':
    app()