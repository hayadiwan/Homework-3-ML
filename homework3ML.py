import random
import math

def calculateT(fileList, offset):
	A = offset
	B = offset
	C = offset
	D = offset

	for line in fileList:
		line = line.split(',')

		if int(line[1]) == 1:
			if int(line[2]) == 1:
				A+=1
			else:
				C+=1
		else:
			if int(line[2]) == 1:
				B+=1
			else:
				D+=1
	T = (A*D) / (B*C)

	return T

def calculateTEstimates(fileList, offset):
	m = [100, 1000, 10000]
	tList = []

	for popSize in m: 
		t = 0
		for subsample in range(0, 10):
			tempList = random.sample(fileList, popSize) #collect random subsample of size m
			t+=calculateT(tempList, offset) #calculate T for that random subsample

		avgT = t/10 #average T across all 10 subsamples
		tList.append(avgT)

	return tList

def calculateAverageErrorList(list1, list2, numberSubsamples):
	error = []

	for i in range(len(list1)):
		error.append(abs(list1[i] - list2[i])/numberSubsamples)

	return error

def calculateAverageErrorT(list1, T, numberSubsamples):
	error = []

	for i in range(len(list1)):
		error.append(abs(list1[i] - T)/numberSubsamples)

	return error

if __name__ == "__main__":
	f = open("covid_data.csv", "r")
	next(f)

	fileList = []

	for line in f:
		fileList.append(line)

	T = calculateT(fileList, 0)
	print("T calculation for dataset provided:")
	print(T)

	TTildeList = calculateTEstimates(fileList, 0)

	print("\nT tilde calculation for each m:")
	print(TTildeList)

	TTildaError = calculateAverageErrorT(TTildeList, T, 10)
	print("\nAverage error between T tilde and T:")
	print(TTildaError)

	ThatList = calculateTEstimates(fileList, 1/0.01)

	print("\nAverage Differentially Private Estimate (T hat) for each m:")
	print(ThatList)

	print("\nAverage error between T hat and T:")
	print(calculateAverageErrorT(ThatList, T, 10))

	print("\nAverage error between T hat and T tilde:")
	print(calculateAverageErrorList(ThatList, TTildeList, 10))




