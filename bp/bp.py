import numpy as np
import random
import math

""" utility functions """
# 2D array normalization, between 0 - 1
def normalize():
    i = 0
    while i < np.size(diabetes,1): # while i < 9, cols
        j = 0
        temp_lst = list() # temp array to hold column values
        while j < np.size(diabetes,0): # while j < 768, rows
            temp_lst.append(diabetes[j][i]) # copy column values per row to list
            j += 1

        temp_max = max(temp_lst) # find maximum value in array
        temp_min = min(temp_lst) # find minimum value in array

        j = 0
        while j < np.size(diabetes,0): # while j < 768, rows
            diabetes[j][i] = (diabetes[j][i]-temp_min)/(temp_max-temp_min) # normalize function
            j += 1

        i += 1

# sigmoid function
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

# hidden layer function
def hidden_layer(arr):
    # initialize weights array with random values [0, 1]
    weights = np.random.rand(np.size(arr),2)

    """ summation function """
    # add all the input * weights
    output = np.matmul(arr, weights) # input X weight, summation function

    # calculate bias
    bias_x = random.uniform(0,1) # bias weight for first hidden layer node
    bias_y = random.uniform(0,1) # bias weight for second hidden layer node

    # add the bias to the total summation
    output[0] = output[0] + bias_x # add bias for node x
    output[1] = output[1] + bias_y # add bias for node y

    """ activation function """
    # pass through the sigmoid function
    output[0] = sigmoid(output[0])
    output[1] = sigmoid(output[1])

    return output

# output layer function
def output_layer(arr):
    # initialize weights array with random values [0, 1]
    weights = np.random.rand(np.size(arr),1)

    """ summation function """
    # add all the input * weights
    output = np.matmul(arr, weights) # input X weight, summation function

    # calculate bias
    bias_x = random.uniform(0,1) # bias weight for first hidden layer node

    # add the bias to the total summation
    output = output + bias_x # add bias for node x

    """ activation function """
    # pass through the sigmoid function
    output = sigmoid(output)

    return output

""" main() """
diabetes = np.loadtxt('diabetes.data.txt') # read data from .txt file into 2D array

normalize() # normalize 2D array

train,test = diabetes[:568,:], diabetes[200:,:] # split data into training, test sets

""" for each row of training data """
k = 0
while k < np.size(train,0): # while k < 568
    # save attributes and class differently
    train_row = train[k]
    expected_output = train_row[np.size(train_row)-1] # row data class

    """ input layer output """
    il_output = train_row[1:9:1] # row data attributes

    """ hidden layer output """
    hl_output = hidden_layer(il_output)

    """ output layer output """
    system_output = output_layer(hl_output)

    """ error """
    error = pow(expected_output-system_output,2) #calculate error
    print(error)

    """ continue doing backpropagation """

    k += 1
