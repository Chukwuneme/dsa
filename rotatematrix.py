import numpy as np

def rotate_matrix(m):
	r = []
	i = 0

	for row in m:
		lis = [item[i] for item in m]
		r.append(lis)
		i += 1

	print(r)

gg = [[1,2,3], [6,7,8], [9,10,11]]
rotate_matrix(gg)
