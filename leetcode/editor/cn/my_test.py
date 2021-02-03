# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# newarr = np.array_split(arr, 4)
#
# print(newarr)


import random


def split(a, n):
    k, m = divmod(len(a), n)
    return [a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in list(range(n))]


list_split = split(list(range(14)), 4)
print(list_split)
