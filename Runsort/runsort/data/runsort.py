import algs4

with open('tiny.txt') as file:
    list = []
    for line in file:
        list.append(line.strip('\n'))

#Soley for comparison of indexes in the array. Treat as array.
def sort(x, y):


#Merge sort:
def merge_sort(list):
    lenght = len(list)
    if lenght == 1:
        return list
    list_1 = list[0:lenght/2]
    list_1 = list[lenght/2+1:lenght]

