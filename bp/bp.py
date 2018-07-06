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
def hidden_layer(arr, w):
    # initialize weights array with random values [0, 1]
    weights = w

    """ summation function """
    # add all the input * weights
    output = np.matmul(arr, weights) # input X weight, summation function

    """ activation function """
    # pass through the sigmoid function
    output[0] = sigmoid(output[0])
    output[1] = sigmoid(output[1])

    return output

# output layer function
def output_layer(arr, w):
    # initialize weights array with random values [0, 1]
    weights = w

    """ summation function """
    # add all the input * weights
    output = np.matmul(arr, weights) # input X weight, summation function

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
    weights_i = np.random.rand(np.size(il_output),2) # weights for input layer output

    """ hidden layer output """
    hl_output = hidden_layer(il_output, weights_i)
    weights_h = np.random.rand(np.size(hl_output),1)

    """ output layer output """
    system_output = output_layer(hl_output, weights_h)

    """ error """
    error = pow(expected_output-system_output,2) # calculate error

    """ backpropagation """
    lr = 0.5 # learning rate - N

    #""" 1. for output layer node """
    d = (expected_output - system_output) * system_output * (1. - system_output) # derivative variance - E = d
    lr_d_temp = lr * d # lr * E(d)

    ciw_h = np.full_like(weights_h, 0)
    ciw_h =  np.multiply(hl_output, lr_d_temp) # change in weight

    # calculate new weight for hidden layer output weights
    weights_h = np.add(weights_h, ciw_h)

    #""" 2. for hidden layer node """
    # calculate e
    e = weights_h * d
    #d = np.dot(weights_i, d) * weights_i * (1. - weights_i) # derivative variance - E = d
    #lr_d_temp = lr * d # lr * E(d)

    #ciw_i = np.full_like(weights_i, 0)
    #ciw_i = np.multiply(lr_d_temp, il_output) # change in weight
    
    # calculate new weight for input layer output weights
    #weights_i = np.add(weights_i, ciw_i)

    print(hl_output)

    k += 1
