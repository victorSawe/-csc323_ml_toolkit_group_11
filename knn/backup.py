import math                                             # import math library
import collections                                      # import collections library
import random                                           # import random library

""" Split the data into Training set and Testing set """
set = list()                                            # empty list

f = open("iris.data.txt", "r")                          # open file
for x in f:                                             # read from file
    set.append(x)                                       # save to list

random.shuffle(set)                                     # shuffle array

f = open("train.txt", "a")                              # create training data set
a = 0
while a < 100:
    f.write(set[a])
    a += 1

f = open("test.txt", "a")                               # create testing data set
b = 100
while b < 150:
    f.write(set[b])
    b += 1

""" Read from Training set """
train_set = list()                                      # empty list

f = open("train.txt", "r")                              # open file
for x in f:                                             # read from training set
    train_set.append(x)                                 # save to list

w, h = 6, 100                                           # columns, rows
training = [[0 for x in range(w)] for y in range(h)]    # initialize multidimensional list

i = 0                                                   # row counter
while i < 100:                                          # while i < no_of_rows
    attribute = train_set[i].split(',')                 # split each set into attributes
    j = 0                                               # column counter
    while j < 5:                                        # while i < no_of_columns
        training[i][j] = attribute[j]                   # save values in training matrix
        j += 1                                          # increment column counter
    i += 1                                              # increment row counter

""" Read from Testing set """
test_set = list()                                       # empty list

f = open("test.txt", "r")                               # open file
for x in f:                                             # read from training set
    test_set.append(x)                                  # save to list

w, h = 6, 50                                            # columns, rows
testing = [[0 for x in range(w)] for y in range(h)]     # initialize multidimensional list

i = 0                                                   # row counter
while i < 50:                                           # while i < no_of_rows
    attribute = test_set[i].split(',')                  # split each set into attributes
    j = 0                                               # column counter
    while j < 5:                                        # while i < no_of_columns
        testing[i][j] = attribute[j]                    # save values in training matrix
        j += 1                                          # increment column counter
    i += 1                                              # increment row counter

l = 0
m = 0
while m < 50:
    while l < 150:

        training[l][5] = math.sqrt(                     # calculate the euclidean distance
        math.pow((float(testing[m][0]) - float(training[l][0])), 2)
        + math.pow((float(testing[m][1]) - float(training[l][1])), 2)
        + math.pow((float(testing[m][2]) - float(training[l][2])), 2)
        + math.pow((float(testing[m][3]) - float(training[l][3])), 2))

        l += 1
    m += 1

    training = sorted(training, key=lambda sin: sin[5])     # sort array using distance training[5]

    # K
    k = 50

    n = 0
    classes = list()
    while n < k:
        classes.append(training[n][4])                      # save classes of select training in new list
        n += 1

    common = collections.Counter(classes)
    result = common.most_common(3)

    print(result[0][0])                                     # print the most popular class
