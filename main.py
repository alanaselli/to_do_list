#!/usr/bin/env python
# coding: utf-8

# To-do-list Project

# Goal:
# To create a tool to organize daily, weekly, and monthly activities

# Dates on iso format: 'YYYY-MM-DD'
# Names of the week: Monday, Tuesday…

# Import modules
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

days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def save_file():
    with open("date_tasks.json", "w") as outfile:
        json.dump(date_tasks, outfile)

def main(a):
    for i in a.t:
        date_tasks[a.d.isoformat()].append(i)
        print(i + " added to " + a.d.isoformat() + " list!")
    save_file()

def show_tasks(a):
    list_of_the_day = date_tasks[a.d.isoformat()]
    for n in range(7):
        if a.d.weekday() == n:
            list_of_the_day.extend(date_tasks[days_of_the_week[n]])
    for i in range(len(list_of_the_day)):
            print("- " + list_of_the_day[i])
    for v in date_tasks[a.d.isoformat() + '_c']:
            print("\033[09m {}\033[00m" .format(v))
    if len(list_of_the_day) == 0:
        print("Your list is empty!")

def add_weekly_task(a):
    for i in a.wd:
        date_tasks[i].append(a.t)
        print(a.t + " added to " + i + " list!")
    save_file()

def remove_task(a):
    date_tasks[a.d.isoformat()].remove(a.t)
    save_file()
    print(a.t + " removed from " + a.d.isoformat() + " list!")

def remove_weekly_task(a):
    for i in a.wd:
        date_tasks[i].remove(a.t)
        print(a.t + " removed from " + i + " list!")
    save_file()

def remove_day_tasks(a):
    del date_tasks[a.d.isoformat()]
    save_file()
    print("All tasks removed from "+a.d.isoformat()+" list!")

def empty_all():
    date_tasks.clear()
    save_file()
    print("All tasks were deleted.")

def check_task(a):
    item_name = a.d.isoformat() + '_c'
    for i in a.t:
        date_tasks[item_name].append(i)
        if i in date_tasks[a.d.isoformat()]:
            date_tasks[a.d.isoformat()].remove(i)
        print(i + " checked from " + a.d.isoformat() + " list!")
    save_file()

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
        help='a task to perform',
        nargs='*'
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
    parser.add_argument(
        '-c',
        action='store_true',
        help='check tasks'
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
    elif args.c:
        check_task(args)
    elif args.t:
        main(args)
    elif args.d:
        show_tasks(args)
    else:
        print('''
                            --- Welcome to your to-do list! ---

        You can start a to-do list by typing a date in the YYYY-MM-DD format and a task.
        Use the flags -d and -t to specify your arguments.
        Here's an example:
        -d 2000-10-01 -t study

        To view the list for the day, simply type the -d flag and the date.

        You can find more help using the -h flag.

        Good luck on your tasks!
        ''')
