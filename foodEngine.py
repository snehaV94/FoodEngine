# adding comment for editing check
import operator
import functools 
import numpy as np
alpha = 0.00000005
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
	for i in range (0,theta.shape[0]):
		tempTheta[i]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,i:i+1].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	for i in range (0,theta.shape[0]):	
		theta[i]=theta[i]-tempTheta[i]
	#tempTheta[1]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,1:2].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	#tempTheta[2]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,2:3].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount	
	#tempTheta[3]=  [(alpha/inputSampleSize)*sum(sum((((dotProduct(X,theta)-y) * X[:,3:4].reshape(inputSampleSize,nutrientCount)))))]*nutrientCount
	#theta[0]=theta[0]-tempTheta[0]
	#theta[1]=theta[1]-tempTheta[1]
	#theta[2]=theta[2]-tempTheta[2]
	#theta[3]=theta[3]-tempTheta[3]

	
def getXandY(inputFoodList, duplicateSampleCount):
	dailyLimitList=[1200.0, 325.0, 300.0, 550.0, 2.0, 2500.0, 20.0, 2.0, 10.0, 400.0, 400.0, 25.0, 10.0, 350.0, 5.0, 16.0, 6.0, 1000.0, 3500.0, 56.0, 1.6, 55.0, 2400.0, 35.0, 500.0, 2.0, 60.0, 90.0, 900.0, 6.0, 2.0, 12.0, 120.0, 15.0, 30]
	food_items=open("nutrient_data.txt").read().split('\n')
	food_items=[food_item.split("^") for food_item in food_items]
	food_dict={}
	[food_dict.update({food_item[0]: food_item}) for food_item in food_items]
	X=np.array([[[z*float(food_dict[x][y] )for y in range(4,39)] for x in inputFoodList] for z in range(1,duplicateSampleCount+1)])
	y=np.array([[x*m for x in dailyLimitList] for m in range (1, duplicateSampleCount+1)])
	return (X,y)
	
	

X,y=getXandY(["11741","15077","11234","11215","11365","09050","17243"],2)
inputSampleSize=X.shape[0]		# Number of samples
foodCount=X.shape[1]			# no of food items(features) you are giving to find out the optimal
nutrientCount=X.shape[2] 		# how many nutrients you gonna find out	
theta= np.array([[i]*nutrientCount for i in np.random.rand(foodCount)])
	 

#X=np.array([[[1,2,3],[2,3,1],[3,1,2],[1,3,2]],[[3,1,2],[1,2,3],[2,3,1],[1,3,2]]])
#y=np.array([[18, 23, 19],[15, 26, 19]])
#theta= np.array([[i]*nutrientCount for i in np.random.rand(foodCount)])

print (theta)

for i in range(1000000):
	if (i>70000):
		alpha=0.00000009
	print(str(i)+" cost",computeCost(X, theta,y))
	gradientDescent(X,y,theta)
print(theta)
