#!/usr/bin/env python
# coding: utf-8

# # To-do-list Project
# 
# ## Goal:
# To create an easy to use tool to organize daily, weekly, and monthly activities

# Import modules
import pandas as pd
import numpy as np
import sys
import os.path
import simplejson as json
from collections import defaultdict


# Verify if date_taks exist
# if os.path.exists('date_taks.json'): # True or False
json_path = 'date_tasks.json'
if os.path.exists(json_path):
    with open('date_tasks.json', 'r') as f:
        old_json = json.loads(f.read()) # Open file if exists, create if doesn't exist
        # TODO: how to transform dict -> defaultdict.
        old_json = defaultdict(list, old_json)
        # IMPORTANT: this is how one opens up a debugger: `import pdb; pdb.set_trace()`.
else:
    old_json = defaultdict(list)


def add_one_time_task(day, task):
    date_tasks[day].append(task)
    print(date_tasks[day])
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

# Run from terminal
if sys.argv[1] in ['TASK','Task','task']:
    day = sys.argv[2]
    task = sys.argv[3]
    add_one_time_task(day, task)