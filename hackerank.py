a = [1,2,2,3,4,4]
b = [2,5]

def matches(A, B):
	A.sort()
	out = []
	for i in B:
		summ = 0
		for j in A:
			if j <= i:
				summ += 1
		out.append(summ)

	print(out)

matches(a, b)


def matches(A, B):
	A.sort()
	prev = "P"
	prev_num = 0
	mat = {}
	dd = []
	out = []




	def binary_search(arr, num):
		if len(arr) == 0:
			return 0
		mid = len(arr) // 2


		if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid  + 1]:
			return arr[mid - 1]
		elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid  + 1]:
			binary_search(arr[:mid], num)
		elif arr[mid] < arr[mid - 1] and arr[mid] < arr[mid  + 1]:
			binary_search(arr[mid + 1], num)


	for i in A:
		if i != prev:
			mat[i] = prev_num
			mat[i] += 1
			prev = i
			prev_num = mat[i]
		else:
			mat[i] += 1
			prev = i
			prev_num = mat[i]

	for i in B:
		if i in mat:
			out.append(mat[i])
		else:
			dd = binary_search(mat, i)
			out.append(dd)

	print(out)





matches(a, b)