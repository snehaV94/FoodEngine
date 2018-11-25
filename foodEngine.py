import operator
import functools 
import numpy as np
import tensorflow
alpha = 0.01
iters = 1000


def computeCost(X, theta,y):
	pred=dotProduct(X,theta)
	return sum(sum((y-pred)**2))

def dotProduct(X,theta):
	product=X*theta
	return np.array([functools.reduce(operator.add,lis) for lis in product])

def mean(X):
	return sum(sum(X))/2

def variance(X,mean):
	return sum((X-mean)**2)

def gradientDescent(X,y,theta):
	print("check this", sum(sum((((dotProduct(X,theta)-y) * X[:,0:1].reshape(inputSampleSize,nutrientCount))))))
	theta[0]= theta[0]- [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,0:1].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	theta[1]= theta[1]- [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,1:2].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	theta[2]= theta[2]- [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,2:3].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount


	
inputSampleSize=1		# Number of samples
foodCount=3    			# no of food items(features) you are giving to find out the optimal
nutrientCount=4 		# how many nutrients you gonna find out	

#X=np.array([[[2,3,3],[1,2,4],[1,3,5]],[[1,7,3],[2,7,3],[1,0,4]]])		#original
#y=np.array(([[13,54,46],[1,3,5]]))  									#original
#theta= np.array([[i]*nutrientCount for i in np.random.rand(foodCount)])#original 

X=np.random.random_integers(10, size=(inputSampleSize,foodCount,nutrientCount))	#test
y=np.random.random_integers(10, size=(inputSampleSize,nutrientCount))			#test	 
theta= np.array([[1.0]*nutrientCount for i in range(0,foodCount)])				#test

for i in range(300):
	if i >28:
		alpha=.1
	print (theta)
	print (computeCost(X, theta,y))
	gradientDescent(X,y,theta)





def t(theta):
    theta[0]=[1,2,34,4]

















