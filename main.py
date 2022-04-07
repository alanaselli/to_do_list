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

days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# function to be called inside other functions, open the file
def open_file(a):
    # Verify if date_tasks exist
    json_path = a.f
    if os.path.exists(json_path):
        with open(a.f, 'r') as f:
            date_tasks = json.loads(f.read())
            date_tasks = defaultdict(list, date_tasks)
            return date_tasks
            # IMPORTANT: this is how one opens up a debugger: `import pdb; pdb.set_trace()`.
    else:
        date_tasks = defaultdict(list)
        return date_tasks

# function to be called inside other functions, save the file
def save_file(date_tasks, a):
    with open(a.f, "w") as outfile:
        json.dump(date_tasks, outfile)

# for every task in tasks list, add task to date list
def main(a):
    date_tasks = open_file()
    for i in a.t:
        date_tasks[a.d.isoformat()].append(i)
        print(i + " added to " + a.d.isoformat() + " list!")
    save_file(date_tasks)

# Show tasks for a given date
def show_tasks(a):
    date_tasks = open_file()
    list_of_the_day = date_tasks[a.d.isoformat()]
    # Iterate through the days of the week to add weekly tasks to the list
    for n in range(7):
        if a.d.weekday() == n:
            list_of_the_day.extend(date_tasks[days_of_the_week[n]])
    # Print each task in a line
    for i in range(len(list_of_the_day)):
            print("- " + list_of_the_day[i])
    # Print checked tasks with striketrhough format
    for v in date_tasks[a.d.isoformat() + '_c']:
            print("\033[09m {}\033[00m" .format(v))
    # If the list is empty, print this statement
    if len(list_of_the_day) == 0:
        print("Your list is empty!")

# Add weekly tasks providing one or more days of the week
def add_weekly_task(a):
    date_tasks = open_file()
    # For each day provided
    for i in a.wd:
        # For each task provided
        for t in a.t:
            # Append task to the day list
            date_tasks[i].append(t)
        print(t + " added to " + i + " list!")
    save_file(date_tasks)

# Remove task(s) from list
def remove_task(a):
    date_tasks = open_file()
    # For each task provided
    for i in a.t:
        # Try to remove from day list
        try:
            date_tasks[a.d.isoformat()].remove(i)
        # If it doesn't work, check the checked lists
        except:
            date_tasks[a.d.isoformat() + '_c'].remove(i)
    print(i + " removed from " + a.d.isoformat() + " list!")
    save_file(date_tasks)

# Remove weekly tasks
def remove_weekly_task(a):
    date_tasks = open_file()
    # For each day provided
    for i in a.wd:
        # For each task provided
        for t in a.t:
            # Remove task
            date_tasks[i].remove(t)
        print(t + " removed from " + i + " list!")
    save_file(date_tasks)

# Remove all tasks for a given day
def remove_day_tasks(a):
    date_tasks = open_file()
    del date_tasks[a.d.isoformat()]
    save_file(date_tasks)
    print("All tasks removed from "+a.d.isoformat()+" list!")

# Remove all lists
def empty_all():
    date_tasks = open_file()
    print("WARNING! This will delete all your lists!")
    yesChoice = ['yes', 'y']
    noChoice = ['no', 'n']

    user_answer = input("Do you wish to continue? [y/n] ").lower()

    if user_answer in yesChoice:
        date_tasks.clear()
        save_file(date_tasks)
        print("All tasks were deleted.")
    elif user_answer in noChoice:
        print("Exiting the program.")
        exit(0)
    else: 
        print("Invalid input.\nAborting program.")
        exit(1)

# Check completed tasks
def check_task(a):
    date_tasks = open_file()
    # Create a name with the date plus '_c'
    item_name = a.d.isoformat() + '_c'
    # For each task provided
    for i in a.t:
        # Append to new list with created name
        date_tasks[item_name].append(i)
        # If the task is in the regular day list, remove it
        if i in date_tasks[a.d.isoformat()]:
            date_tasks[a.d.isoformat()].remove(i)
        print(i + " checked from " + a.d.isoformat() + " list!")
    save_file(date_tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create To-do Lists')
    parser.add_argument(
        '-f','-FILE',
        type=str,
        help='the name of the file you want to save your lists into'
    )
    parser.add_argument(
        '-d','-DATE',
        type=date.fromisoformat, 
        help='a date for a task'
    )
    parser.add_argument(
        '-t','-TASK',
        type=str,
        help='a task to perform',
        nargs='*' # Allows for 0 or more arguments
    )
    parser.add_argument(
        '-wd','-WEEKDAY',
        type=str, 
        choices=days_of_the_week.values(),
        nargs="*", # Allows for 0 or more arguments
        help='one or more days of the week'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-r','-REMOVE',
        action='store_true',
        help='remove a task'
    )
    group.add_argument(
        '-c','-CHECK',
        action='store_true',
        help='check tasks'
    )
    parser.add_argument(
        '-empty','-EMPTY',
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
