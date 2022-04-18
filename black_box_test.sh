#!/bin/bash

printf "The file used will be test.json. All data in this file will be deleted.
Do you wish to continue?[y/n]\n"

read useranswer

if [ $useranswer = "y" ]
then
    printf "\nStarting tests…\n"
else
    printf "\nAborting program\n"
    exit
fi

printf "\nAdding a task:\n"
printf "python3.8 main.py -f test -d 2022-03-29 -t task_1\n"
python3.8 main.py -f test -d 2022-03-29 -t task_1

printf "\nPrinting list:\n"
printf "python3.8 main.py -f test -d 2022-03-29\n"
python3.8 main.py -f test -d 2022-03-29

printf "\nChecking task:\n"
printf "python3.8 main.py -f test -d 2022-03-29 -t task_1 -c\n"
python3.8 main.py -f test -d 2022-03-29 -t task_1 -c

printf "\nPrinting list:\n"
printf "python3.8 main.py -f test -d 2022-03-29\n"
python3.8 main.py -f test -d 2022-03-29

printf "\nAdding weekly task:\n"
printf "python3.8 main.py -f test -t task_2 -wd Tuesday Friday\n"
python3.8 main.py -f test -t task_2 -wd Tuesday Friday

printf "\nPrinting Tuesday list:\n"
printf "python3.8 main.py -f test -d 2022-03-29\n"
python3.8 main.py -f test -d 2022-03-29

printf "\nPrinting Friday list:\n"
printf "python3.8 main.py -f test -d 2022-04-01\n"
python3.8 main.py -f test -d 2022-04-01

printf "\nRemoving weekly task:\n"
printf "python3.8 main.py -f test -t task_2 -wd Friday -r\n"
python3.8 main.py -f test -t task_2 -wd Friday -r

printf "\nRemoving all tasks from a given date:\n"
printf "python3.8 main.py -f test -d 2022-03-29 -r\n"
python3.8 main.py -f test -d 2022-03-29 -r

printf "\nPrinting list:\n"
printf "python3.8 main.py -f test -d 2022-03-29\n"
python3.8 main.py -f test -d 2022-03-29

printf "\nEmptying list:\n"
printf "python3.8 main.py -f test -e -q\n"
python3.8 main.py -f test -e -q