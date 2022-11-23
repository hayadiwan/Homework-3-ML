import numpy as np

n = 4
A = np.random.randint(-100, 100, size=[n, n+1]) #create some n*m matrix

print(A)

def calculateg(A, x):
	gNum = x.transpose() @ A.transpose() @ A @ x
	gDenom = x.transpose() @ x
	g = - (gNum / gDenom)

	return g

def is_convex(A, x, y, lambdA):
	#use original convextiy equation 
	if (1 - lambdA) * calculateg(A, x) + lambdA * calculateg(A, y) <= calculateg(A, ((1-lambdA) * x) + (lambdA * y)):
		return True
	else:
		return False

#just two random lines y = x, y = 3x
px = np.array([1, 2, 3, 4, 5])
py = np.array([3, 9, 12, 15, 18])

for i in range(2, 10):
	lambdA = 1/i

	if is_convex(A, px, py, lambdA):
		print("convex")
	else:
		print("not convex")


