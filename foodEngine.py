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



203^g^PROCNT^Protein^56
204^g^FAT^Total_lipid_fat_^60
205^g^CHOCDF^Carbohydrate_by_difference^325
208^kcal^ENERC_KCAL^Energy^2500
263^mg^THEBRN^Theobromine^500
269^g^SUGAR^Sugars^35
291^g^FIBTG^dietary_Fiber^30
301^mg^CA^Calcium^1200
303^mg^FE^Iron^25
304^mg^MG^Magnesium^350
305^mg^P^Phosphorus^1000
306^mg^K^Potassium^3500
307^mg^NA^Sodium^2400
309^mg^ZN^Zinc^15
312^mg^CU^Copper^2
313^mcg^FLD^Fluoride^10
315^mg^MN^Manganese^5
317^mcg^SE^Selenium^55
318^IU^VITA_IU^Vitamin_A^900
323^mg^TOCPHA^Vitamin_E^12
337^mcg^LYCPN^Lycopene^10
401^mg^VITC^Vitamin Ctotal_ascorbic_acid^90
404^mg^THIA^Thiamin^2
405^mg^RIBF^Riboflavin^1.6
406^mg^NIA^Niacin^16
410^mg^PANTAC^Pantothenic_acid^6
415^mg^VITB6A^Vitamin_B_6^2
417^mcg^FOL^Folate^400
418^mcg^VITB12^Vitamin_B_12^6
421^mg^CHOLN^Choline^550
430^mcg^VITK1^Vitamin_K^120
431^mcg^FOLAC^Folic_acid^400
601^mg^CHOLE^Cholesterol^300
605^g^FATRN^Fatty_acids_trans^2
606^g^FASAT^Fatty_acids_total_saturated^20
