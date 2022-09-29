def kth_permutation(n, k):
		
	nums = [c for c in range(1, n + 1)]
	words = []
	k = k - 1
	
	def helper(n, k):
		
		def factorial(n):
			h = 1
			for a in range(1, n + 1):
				h = a * h
			return h
	
		b = factorial(n - 1)
		print(b)
	
		f = k // b
	
		words.append(nums[f])
		
		n = n - 1
		k = k % b
		
		nums.pop(f)
		if n == 1:
			words.append(nums[0])
			return
			
		helper(len(nums), k)
	
	helper(n, k)
	return words

print(kth_permutation(4, 3))