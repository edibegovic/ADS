import subprocess
import time

def run_test(alg, size, number_of_tests):
    total = 0.0
    for i in range(0, number_of_tests):
        start = time.time()
        subprocess.call("python Generator.py " + str(size) + " | python " + alg, shell=True)
        end = time.time()
        print("curr: ", (end-start))
        total += (end - start)

    print("\n", alg, "\n Avrege time for N =" , size, ": ", total/number_of_tests, "\n\n")

# -------------- READ ME -----------------
# 1st PARAM: algorithm (filename)
# 2nd PARAM: size of test (N)
# 3rd PARAM: number of times to repeat experiment

run_test("foursum_fast.py", 20, 6)
run_test("foursum_fast.py", 50, 6)
run_test("foursum_fast.py", 100, 6)
run_test("foursum_fast.py", 130, 6)
run_test("foursum_fast.py", 200, 6)
run_test("foursum_fast.py", 250, 6)
run_test("foursum_fast.py", 300, 6)

run_test("foursum_simple.py", 20, 6)
run_test("foursum_simple.py", 50, 6)
run_test("foursum_simple.py", 100, 6)
run_test("foursum_simple.py", 130, 6)
run_test("foursum_simple.py", 200, 6)
run_test("foursum_simple.py", 250, 6)
run_test("foursum_simple.py", 300, 6)