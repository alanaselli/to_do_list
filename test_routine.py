from ast import Continue
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

print("\nEmpting lists")
empty_test = os.system("python3.8 main.py -empty")
print("Empting list ran with exit code %d" % empty_test)

print("\033[1m" + "\ntest_1: "  + "\033[0m" + "python3.8 main.py -d 2022-03-30 -t task_1")
test_1 = os.system("python3.8 main.py -d 2022-03-30 -t task_1")
print("`test_1` ran with exit code %d" % test_1)

print("\033[1m" + "\ntest_2: "  + "\033[0m" + "python3.8 main.py -d 2022-03-30")
test_2 = os.system("python3.8 main.py -d 2022-03-30")
print("`test_2` ran with exit code %d" % test_2)

print("\033[1m" + "\ntest_3: "  + "\033[0m" + "python3.8 main.py -t every_tuesday -wd Tuesday")
test_3 = os.system("python3.8 main.py -t every_tuesday -wd Tuesday")
print("`test_3` ran with exit code %d" % test_3)

print("\033[1m" + "\ntest_4: "  + "\033[0m" + "python3.8 main.py -t every_wed_fri -wd Wednesday Friday")
test_4 = os.system("python3.8 main.py -t every_wed_fri -wd Wednesday Friday")
print("`test_4` ran with exit code %d" % test_4)

print("\033[1m" + "\ntest_5: "  + "\033[0m" + "python3.8 main.py -d 2022-03-29")
test_5 = os.system("python3.8 main.py -d 2022-03-29")
print("`test_5` ran with exit code %d" % test_5)

print("\033[1m" + "\ntest_6: "  + "\033[0m" + "python3.8 main.py -d 2022-03-30")
test_6 = os.system("python3.8 main.py -d 2022-03-30")
print("`test_6` ran with exit code %d" % test_6)

print("\033[1m" + "\ntest_7: "  + "\033[0m" + "python3.8 main.py -d 2022-04-01")
test_7 = os.system("python3.8 main.py -d 2022-04-01")
print("`test_7` ran with exit code %d" % test_7)