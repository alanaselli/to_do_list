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

print("\nEmptying lists")
empty_test = os.system("python3.8 main.py -empty")
print("Empting list ran with exit code %d" % empty_test)

list_of_tests = [
    "python3.8 main.py -d 2022-03-29 -t this_is_a_task",
    "python3.8 main.py -d 2022-03-29",
    "python3.8 main.py -t every_tue_fri -wd Tuesday Friday",
    "python3.8 main.py -d 2022-03-29",
    "python3.8 main.py -d 2022-04-01",
    "python3.8 main.py -t every_tue_fri -wd Tuesday Friday -r",
    "python3.8 main.py -d 2022-03-29 -t this_is_a_task -r",
    "python3.8 main.py -d 2022-03-29 -r"
]

list_of_errors = {}
for i in list_of_tests:
    print("\033[1m" + "\nTest_" + str(list_of_tests.index(i)+1) + ": "  + "\033[0m" + i)
    # print("Test_" + str(list_of_tests.index(i)+1) + " ran with exit code %d" % os.system(i))
    er = '%d' % os.system(i)
    if er != '0':
        list_of_errors[list_of_tests.index(i)+1] = er
if len(list_of_errors) == 0:
    print("\n--- All tests ran without errors! ---")
else:
    for k,v in list_of_errors.items():
        print("\nTest_"+ str(k) + " ran with exit code " + v)

print("\nEmptying all lists…")
os.system("python3.8 main.py -empty")
print("\nTest routine completed!\n")

# print("\033[1m" + "\ntest_2: "  + "\033[0m" + "python3.8 main.py -d 2022-03-30")
# test_2 = os.system("python3.8 main.py -d 2022-03-30")
# print("`test_2` ran with exit code %d" % test_2)

# print("\033[1m" + "\ntest_3: "  + "\033[0m" + "python3.8 main.py -t every_tuesday -wd Tuesday")
# test_3 = os.system("python3.8 main.py -t every_tuesday -wd Tuesday")
# print("`test_3` ran with exit code %d" % test_3)

# print("\033[1m" + "\ntest_4: "  + "\033[0m" + "python3.8 main.py -t every_wed_fri -wd Wednesday Friday")
# test_4 = os.system("python3.8 main.py -t every_wed_fri -wd Wednesday Friday")
# print("`test_4` ran with exit code %d" % test_4)

# print("\033[1m" + "\ntest_5: "  + "\033[0m" + "python3.8 main.py -d 2022-03-29")
# test_5 = os.system("python3.8 main.py -d 2022-03-29")
# print("`test_5` ran with exit code %d" % test_5)

# print("\033[1m" + "\ntest_6: "  + "\033[0m" + "python3.8 main.py -d 2022-03-30")
# test_6 = os.system("python3.8 main.py -d 2022-03-30")
# print("`test_6` ran with exit code %d" % test_6)

# print("\033[1m" + "\ntest_7: "  + "\033[0m" + "python3.8 main.py -d 2022-04-01")
# test_7 = os.system("python3.8 main.py -d 2022-04-01")
# print("`test_7` ran with exit code %d" % test_7)