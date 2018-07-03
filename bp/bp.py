"""
The following is an implementation of the Backward Propagation algorithm

The dataset that can be used with this algorithm must be in the format:

[ attr_1, attr_2, attr_3, attr_4, class ]

"""
import math
import collections
import random

""" read data from file  """
iris = list() # empty list

f = open('iris.data.txt', 'r') # open file
for x in f: # read from file
    iris.append(x) # save to list

random.shuffle(iris) # shuffle list

""" create training set """
a, b = 5, 100
train = [[0 for w in range(a)] for x in range(b)] # initialize training set list

i = 0
while i < b:
    tr_attribute = iris[i].split(',')
    j = 0
    while j < 5:
        train[i][j] = tr_attribute[j]
        j += 1
    i += 1

""" create testing set """
c, d = 5, 50
test = [[0 for y in range(c)] for z in range(d)] # initialize testing set list

k = 0
m = b
while k < d:
    tst_attribute = iris[m].split(',')
    l = 0
    while l < c:
        test[k][l] = tst_attribute[l]
        l += 1
    k += 1
    m += 1
