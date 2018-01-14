Arr = [2, 5 ,7 , 8, 10, 15]
N = 6
Sum = 15

DP = {}

for i in range(N):
	DP[i,0] = True

for i in range(N):
	for j in range(1,Sum+1):
		if i == 0 :
			if j == Arr[i]:
				DP[i,j] = True
			else:
				DP[i,j] = False
		else:
			if j < Arr[i]:
				DP[i,j] = DP[i-1,j]
			else:
				DP[i,j] = DP[i-1,j] | DP[i-1,j-Arr[i]]

count = 0

for i in range(N):
	if DP[i,Sum] :
		count = count + 1

print(count)		