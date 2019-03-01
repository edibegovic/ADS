from __future__ import print_function
import sys
from algs4.sorting import merge
#from algs4.searching import binary_search_st

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

# for i in range(0, N):
#      for j in range(i+1, N):
#          for k in range(j+1, N):
#              for l in range(k+1, N):
#                  if vals[i]+vals[j]+vals[k]+vals[l] == 0:
#                      print(i,j,k,l,file=sys.stderr)
#                      print(True)
#                      sys.exit()
# print(False)

merge.sort(vals)

def binary_search_recursive(needle, haystack, index = 0):
    global midway
    midway = (len(haystack)) // 2
    if midway < 2:
        return False
    if haystack[midway] == needle:
        return True
    else:
        if needle > haystack[midway]:
            return binary_search_recursive(needle, haystack[midway:], index + midway)            
        else:
            return binary_search_recursive(needle, haystack[:midway], index)

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            needle = int(vals[i] + vals[j] + vals[k])
            if binary_search_recursive((-1 * needle), vals) == True:
                print(i,j,k,midway,file=sys.stderr)
                print(True)
                sys.exit()
print(False)
            