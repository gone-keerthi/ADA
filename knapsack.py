def knapSack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))
val = [40, 50, 60]
wt = [1, 2, 3]
W = 50
n = len(val)
print (knapSack(W, wt, val, n))


