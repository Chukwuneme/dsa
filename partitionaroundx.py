ls = [2,3,4,5,6,5,4,3,2,3,4,5,6]

def partiitionAround(x, arr):
	if len(arr) < 2:
		return False
	for i in range(0, len(ls)):
		if ls[i] < x:
			continue
		else:
			y = ls.pop(i)
			ls.append(y)
	return arr

print(partitionAround(3, arr))

