#importing dependancies


#for matrix algebra
import numpy as np

#for data manipulation
import pandas as pd

from scipy.spatial import distance
import matplotlib.pyplot as plt


#set seed to be random
#np.random.seed(1345)


#load the data using pandas
heart_data=pd.read_csv("heart.csv",header=None)

#show data structure
#print(heart_data.head())


#show mean etc...
#print(heart_data.describe())


#WEIGHTS/ NODE CLASS



#STEP ONE: NORMALIZING DATA IN THE DATA FRAME


heart_data_normalized =(heart_data - heart_data.mean()) / (heart_data.max() - heart_data.min())


#print("NORMALIZED SAMPLE DATA")
#print(heart_data_normalized.head())
#show mean etc...
#print(heart_data_normalized.describe())










#STEP TWO: INITIALIZING WEIGHTS
#The weights will be a matrix with the dimensions inputdimensions by number of nodes

#number of output nodes
nodes_num= 4
#number of input dimensions
input_dimensions=len(heart_data_normalized.columns)

#learning rate
learning_rate_initialized=0.3

weight_matrix=np.random.rand(input_dimensions, nodes_num)


print("INITIALIZED WEIGHT MATRIX:")
print(weight_matrix)

plt.imshow(weight_matrix, interpolation='none')
plt.savefig("init.png")
    # teacher signal


#STEP THREE : DETERMINE NUMBER OF ITERATIONS
iterations=5*len(heart_data_normalized.index)
print("NUMBER OF ITERATIONS: ")
print(iterations)



#STEP FOUR: BEGIN THE ITERATIVE STAGE:


for (x) in range(iterations):

	#initialize the lowest Euclidean Distance
	dist_BMU= float("inf")

	#STEP 4(A): CHOOSE A RANDOM VALUE FROM THE DATA SET
	random_row_index= np.random.randint(len(heart_data_normalized.index))
	random_row= heart_data_normalized.loc[[random_row_index]]


	#STEP 4(B): Find the Best Matching Unit

	for weight_vector in range(nodes_num):
		dist = distance.euclidean(random_row, weight_matrix[:,weight_vector])
		if (dist < dist_BMU):
			dist_BMU=dist
			weight_BMU= weight_matrix[:, weight_vector]
			index_BMU= weight_vector




	#STEP 4(C): Find the radius of the BMU
	# We skip this because we are using few nodes


	#STEP 4(D): Find the learning rate

	learning_rate=learning_rate_initialized*np.exp(-x/iterations)


	#STEP 4(E): Change the weight vectors in accordance to the function
	weight_matrix[:,index_BMU] = np.add(weight_BMU, learning_rate*(np.subtract(random_row,weight_BMU)))


print("FINAL WEIGHT MATRIX")

print(weight_matrix)
plt.imshow(weight_matrix, interpolation='none')
plt.savefig("final.png")
