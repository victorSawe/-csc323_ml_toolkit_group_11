"""
The following is an implementation of the KNN algorithm

The dataset that can be used with this algorithm must be in the format:

[ attr_1, attr_2, attr_3, attr_4, class ]

The algorithm includes a sixth column [ distance ] for the training data

"""
import math
import collections
import random

""" read from file, create two datasets  """
iris = list() # empty list

f = open('iris.data.txt', 'r') # open file
for x in f: # read from file
    iris.append(x) # save to list

random.shuffle(iris) # shuffle array

""" create training set """
a, b = 6, 100
train = [[0 for w in range(a)] for x in range(b)] # initialize training set list

i = 0
while i < b:
    tr_attribute = iris[i].split(',')
    j = 0
    while j < 5:
        train[i][j] = tr_attribute[j]
        j += 1
    i += 1

""" create test set """
c, d = 5, 50
test = [[0 for y in range(c)] for z in range(d)] # initialize testing set list

k = 0
m = b
while k < d:
    tst_attribute = iris[m].split(',')
    l = 0
    while l < 5:
        test[k][l] = tst_attribute[l]
        l += 1
    k += 1
    m += 1

""" calculate euclidean distance for each test data """
successful = 0
failed = 0
n = 0
while n < d:
    p = 0
    while p < b:
        train[p][5] = math.sqrt(
        math.pow((float(test[n][0]) - float(train[p][0])), 2)
        + math.pow((float(test[n][1]) - float(train[p][1])), 2)
        + math.pow((float(test[n][2]) - float(train[p][2])), 2)
        + math.pow((float(test[n][3]) - float(train[p][3])), 2))
        p += 1


    """ sort train array in asc order of euclidean distance train[][5] """
    train = sorted(train, key=lambda sin: sin[5])

    """ select K nearest neighbour """
    k_options = [1, 3, 5, 7]
    val_k = random.choice(k_options) # chose random value from the options

    q = 0
    classes = list() # initialize empty list
    while q < val_k:
        classes.append(train[q][4]) # append all the top 'K' classes to list
        q += 1

    common = collections.Counter(classes) # initialize Counter with classes
    result = common.most_common(1) # select most common class

    if test[n][4] == result[0][0]:
        successful += 1
        print('Successful Prediction') # success
    else:
        failed += 1
        print('Failed Prediction') # failure

    n += 1

print('==========')
print('{} predictions are successful, and {} predictions fail when K is {}' . format(successful, failed, val_k))
