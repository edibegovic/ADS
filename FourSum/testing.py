import subprocess
import time

d100 = ["Assignment/data/ints-100-0.txt",
"Assignment/data/ints-100-1.txt",
"Assignment/data/ints-100-2.txt",
"Assignment/data/ints-100-3.txt",
"Assignment/data/ints-100-4.txt"
]

d200 = ["Assignment/data/ints-200-1.txt",
"Assignment/data/ints-200-2.txt",
"Assignment/data/ints-200-3.txt",
"Assignment/data/ints-200-4.txt"]

d400 = ["Assignment/data/ints-400-0.txt",
"Assignment/data/ints-400-1.txt",
"Assignment/data/ints-400-2.txt",
"Assignment/data/ints-400-3.txt",
"Assignment/data/ints-400-4.txt"]

d800 = ["Assignment/data/ints-800-0.txt",
"Assignment/data/ints-800-1.txt",
"Assignment/data/ints-800-2.txt",
"Assignment/data/ints-800-3.txt",
"Assignment/data/ints-800-4.txt"]

d1600 = ["Assignment/data/ints-1600-0.txt",
"Assignment/data/ints-1600-1.txt",
"Assignment/data/ints-1600-2.txt",
"Assignment/data/ints-1600-3.txt",
"Assignment/data/ints-1600-4.txt"]

d3200 = ["Assignment/data/ints-3200-0.txt",
"Assignment/data/ints-3200-1.txt",
"Assignment/data/ints-3200-2.txt",
"Assignment/data/ints-3200-3.txt",
"Assignment/data/ints-3200-4.txt"]

def run_test(alg, arr, size):
    total = 0.0
    for test in arr:
        start = time.time()
        subprocess.call("python " + alg + "<" + test, shell=True)
        end = time.time()
        print("curr: ", (end-start))
        total += (end - start)

    print(alg, size, ": ", total/len(arr))

run_test("foursum_simple.py", d100, "100")
run_test("foursum_simple.py", d200, "200")
run_test("foursum_simple.py", d400, "400")
# run_test("foursum_simple.py", d800, "800")
# run_test("foursum_simple.py", d1600, "1600")
# run_test("foursum_simple.py", d3200, "3200")

run_test("foursum_fast.py", d100, "100")
run_test("foursum_fast.py", d200, "200")
run_test("foursum_fast.py", d400, "400")
# run_test("foursum_fast.py", d800, "800")
# run_test("foursum_fast.py", d1600, "1600")
# run_test("foursum_fast.py", d3200, "3200")