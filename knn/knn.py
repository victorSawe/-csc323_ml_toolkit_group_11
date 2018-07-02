import math                                             # import math library

set = list()                                            # empty list

f = open("iris.data.txt", "r")                          # open file
for x in f:                                             # read from file
    set.append(x)                                       # save to list

w, h = 6, 150                                           # columns, rows
data = [[0 for x in range(w)] for y in range(h)]        # initialize multidimensional list

i = 0                                                   # row counter
while i < 150:                                          # while i < no_of_rows
    attribute = set[i].split(',')                       # split each set into attributes
    j = 0                                               # column counter
    while j < 5:                                        # while i < no_of_columns
        data[i][j] = attribute[j]                       # save values in data matrix
        j += 1                                          # increment column counter
    i += 1                                              # increment row counter

s_l = 1.2
s_w = 0.4
p_l = 1
p_w = 0.9

l = 0
while l < 150:                                          # calculate the euclidean distance

    data[l][5] = math.sqrt(
    math.pow((s_l - float(data[l][0])), 2)
    + math.pow((s_w - float(data[l][1])), 2)
    + math.pow((p_l - float(data[l][2])), 2)
    + math.pow((p_w - float(data[l][3])), 2))

    l += 1

data = sorted(data, key=lambda sin: sin[5])             # sort array using distance data[5]

m = 0
while m < 150:
    print(data[m][5])
    m += 1
