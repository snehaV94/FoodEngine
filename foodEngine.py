import operator
import functools 
import numpy as np
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
	tempTheta=np.zeros(shape=theta.shape)
	tempTheta[0]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,0:1].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	tempTheta[1]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,1:2].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	tempTheta[2]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,2:3].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount	
	tempTheta[3]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,3:4].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount


	theta[0]=theta[0]-tempTheta[0]
	theta[1]=theta[1]-tempTheta[1]
	theta[2]=theta[2]-tempTheta[2]
	theta[3]=theta[3]-tempTheta[3]
	print("alpha",alpha)

	
#inputSampleSize=1		# Number of samples
#foodCount=3    			# no of food items(features) you are giving to find out the optimal
#nutrientCount=4 		# how many nutrients you gonna find out	
  									
#theta= np.array([[i]*nutrientCount for i in np.random.rand(foodCount)])#original 

#X=np.random.random_integers(10, size=(inputSampleSize,foodCount,nutrientCount))	#test
#y=np.random.random_integers(10, size=(inputSampleSize,nutrientCount))			#test	 
#theta= np.array([[1.0]*nutrientCount for i in range(0,foodCount)])			#test
X=np.array([[[1,2,3],[2,3,1],[3,1,2],[1,3,2]],[[3,1,2],[1,2,3],[2,3,1],[1,3,2]]])
y=np.array([[18, 23, 19],[15, 26, 19]])
#theta=np.array([[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,1.0]])
inputSampleSize=X.shape[0]		# Number of samples
foodCount=X.shape[1]			# no of food items(features) you are giving to find out the optimal
nutrientCount=X.shape[2] 		# how many nutrients you gonna find out	
#theta= np.array([[1.0]*nutrientCount for i in range(0,foodCount)])
theta= np.array([[i]*nutrientCount for i in np.random.rand(foodCount)])
print (theta)

for i in range(50000):
	if i>100:
		alpha=0.01
	print("cost",computeCost(X, theta,y))
	gradientDescent(X,y,theta)
print(theta)


