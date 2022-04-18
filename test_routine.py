import main
import os

print("WARNING: proceed with caution. Performing this test WILL erase all information from your lists!")
print("Proceed at your own risk.")

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

user_answer = input("Do you wish to continue? [y/n] ").lower()

if user_answer in yesChoice:
    print("\nProceeding with tests…")
elif user_answer in noChoice:
    print("aborting test")
    exit(0)
else: 
    print("Invalid input.\nAborting program.")
    exit(1)

print("\nEmptying lists")
empty_test = os.system("python3.8 main.py -empty -q")
print("Empting list ran with exit code %d" % empty_test)

list_of_tests = [
    "python3.8 main.py -f test -d 2022-03-29 -t this_is_a_task",
    "python3.8 main.py -f test -d 2022-03-29",
    "python3.8 main.py -f test -d 2022-03-29 -t this_is_a_task -c",
    "python3.8 main.py -f test -d 2022-03-29",
    "python3.8 main.py -f test -t every_tue_fri -wd Tuesday Friday",
    "python3.8 main.py -f test -d 2022-03-29",
    "python3.8 main.py -f test -d 2022-04-01",
    "python3.8 main.py -f test -t every_tue_fri -wd Tuesday Friday -r",
    "python3.8 main.py -f test -d 2022-03-29 -t this_is_a_task -r",
    "python3.8 main.py -f test -d 2022-03-29 -r"
]

list_of_errors = {}
for i in list_of_tests:
    print("\033[1m" + "\nTest_" + str(list_of_tests.index(i)+1) + ": "  + "\033[0m" + i)
    er = '%d' % os.system(i)
    if er != '0':
        list_of_errors[list_of_tests.index(i)+1] = er
if len(list_of_errors) == 0:
    print("\n--- All tests ran without errors! ---")
else:
    for k,v in list_of_errors.items():
        print("\nTest_"+ str(k) + " ran with exit code " + v)

print("\nEmptying all lists…")
os.system("python3.8 main.py -empty -q")
print("\nTest routine completed!\n")