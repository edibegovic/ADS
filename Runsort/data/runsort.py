import sys
import algs4

# 🤮
a = [x.strip() for x in sys.stdin]

end_of_first = 0
end_of_second = 0
next_index = 0

while end_of_first != len(a):
    while a[end_of_first] < a[end_of_first + 1]:
       end_of_list += 1
   

def _merge(a, aux, lo, mid, hi):
    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]
        
    # merge back to a[]
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def sort(a):
    """
    Rearranges the array in ascending order, using the natural order.
    
    :param a: the array to be sorted
    """
    n = len(a)
    aux = [None]*n
    
    length = 1
    while length < n:
        lo = 0
        while lo < n-length:
            mid = lo+length-1
            hi = min(mid+length, n-1)
            _merge(a, aux, lo, mid, hi)
            lo += 2*length
        length *= 2
    
    assert _is_sorted(a)

print(a)
