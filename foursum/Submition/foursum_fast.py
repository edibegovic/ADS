from __future__ import print_function
import sys
from algs4.sorting import merge
from algs4.searching import binary_search_st

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

merge.sort(vals)
binarySearch = binary_search_st.BinarySearchST()

for key in vals:
    binarySearch.put(key, key)
       
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            fsum = vals[i] + vals[j] + vals[k]
            if binarySearch.contains(-fsum) and binarySearch.rank(-fsum) > k:
                print(True)
                sys.exit()
print(False)


