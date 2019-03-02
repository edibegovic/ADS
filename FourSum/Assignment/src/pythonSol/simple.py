from __future__ import print_function
import sys
from algs4.sorting import merge

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

# def binary_search_recursive(needle, haystack, index = 0):
#     global midway
#     midway = (len(haystack)) // 2

#     if midway == 0 or len(haystack) == 0:
#         return False

#     if haystack[midway] == needle:
#         return True
#     else:
#         if needle > haystack[midway]:
#             return binary_search_recursive(needle, haystack[midway:], index + midway)            
#         else:
#             return binary_search_recursive(needle, haystack[:midway], index)

       
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            low = k + 1
            high = N - 1
            while low <= high:
                middle = (low + high) // 2
                tot = vals[middle] + vals[i] + vals[j] + vals[k]
                if tot == 0:
                    print(i,j,k,middle,file=sys.stderr)
                    print(True)
                    sys.exit()
                if tot > 0: 
                    high = middle - 1
                if tot < 0:
                    low = middle + 1
print(False)