ls = [2,4,6,8,10,12,13]



def binary(arr, num):
	mid = int((len(arr) / 2) - 0.5)
	hh = None
	while arr[mid] is not num:
		if arr[mid] > num:
			arr = arr[0: mid -1]
			mid = int((len(arr) / 2) - 0.5)
			hh = mid
			#print("idhfdu")
			continue
		elif arr[mid] < num:
			arr = arr[mid + 1:]
			print(arr)
			mid = int((len(arr) / 2) - 0.5)
			if arr[mid] == num:
				hh = mid
				print("rrrrr")
				break
			continue
		
	print("index {}".format(hh))



binary(ls, 13)

begin = 0
end = len(ls) - 1

mid = begin + (end - begin) // 2
print(mid)

print((end - begin) //2)


def decimalToBinary(n):
	return bin(n).replace("0b", "")

print(decimalToBinary(73))

ls = [8,2,4,5,7,3,9,1,10]

leng = len(ls) + 1

for i in range(0, len(ls)):
	current = i
	while current >= 1:
		if ls[current] >= ls [current - 1]:
			break
		elif ls[current] < ls[current - 1]:
			ls[current], ls[current - 1] = ls[current - 1], ls[current]
			current = current - 1
			continue

print(ls)

for i in range(0, len(ls)-1):
	if ls[i] +1 is not ls[i + 1]:
		print(ls[i] + 1)
	else:
		continue
		

def decimalToBinary(n):
	print(bin(n).replace("0b", ""))

decimalToBinary(7888)

def binarygap(num):
	g = []
	while num >= 1:
		h = num % 2
		g.append(h)
		num = num // 2
		#r = "".join(g)
	print(g)
	
	gaps = []
	count = -1
	
	for i in g:
		if i == 1:
			gaps.append(count)
			count = 0
		if i == 0:
			if count == -1:
				continue
			elif count >= 0:
				count +=1
	print(max(gaps))
			

binarygap(3300)


def cyclic(arr, k):
		new_arr = []
		length = len(arr)
		for i in range(0, length):
			print("hjkkk")
			if k + i >= length:
				index = abs(k+i - length)
				new_arr.insert(index, arr[i])
			else:
				new_arr.insert(i + k, arr[i])
		#arr = arr + 1
		print(new_arr)
		return new_arr

cyclic([1,2,3,4,5,6,2,3,4,5,6,4,3], 2)

def cyclicc(arr, k):
	for i in range(0, k):
		arr.insert(0, arr.pop(-1))
		print(arr)

cyclicc([1,2,3,4,5,6], 5)

h = [5,5,6,6,7,7,7]
y = set(h)
t = {}
count = -2

for i in y:
	if h.count(i) % 2 != 0:
		print(i)
		break
	
#print(h.count(5))

from math import modf

def jmp(x,y,d):
	dist = y - x
	if dist % d != 0:
		step = (dist // d) + 1
	else:
		step = dist / d
	return int(step)

print(jmp(1,11,3))


def missing(arr):
	for i in range(0, len(arr)):
		current = i
		while current >= 1:
			if arr[current] >= arr[current - 1]:
				current -= 1
			else:
				arr[current], arr[current -1] = arr[current - 1], arr[current]
				current -= 1
	
	for i in range(0, len(arr)):
		if arr[i + 1] != arr[i] + 1:
			return arr[i] + 1

print(missing([2,3,4,5,6,7,8,10]))

def missing(arr):
	n = len(arr)
	sumtotal = (n+1)*(n+2)/2
	
	sumarray = sum(arr)
	
	print(sumtotal - sumarray)

missing([1,2,3,4,6,7])

def ggg(arr):
	yyy = []
	for p in range(1, len(arr)):
		s = sum(arr[0:p])
		t = sum(arr[p:])
		f = abs(s - t)
		yyy.append(f)
	print(min(yyy))

ggg([5,2,3,4,1])


def quicksort(arr):
	l = len(arr)
	
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()
	
	greater = []
	lesser = []
		
	for i in arr:
		if i > pivot:
			greater.append(i)
		else:
			lesser.append(i)
			
	return quicksort(lesser) + [pivot] + quicksort(greater)
	

print(quicksort([2,4,6,1,6,4,7]))

sett = []
def quicksort(arr, ggg):
	if len(arr) == 0:
		return [0]
	
	if len(arr) == 1:
		ggg.append(arr[0])
		return ggg
	else:
		pivot = arr.pop()
		ggg.append(pivot)
	
	greater = []
	lesser = []
		
	for i in arr:
		if i > pivot:
			greater.append(i)
			if i not in ggg:
				ggg.append(i)
				print(ggg)
		else:
			lesser.append(i)
			if i not in ggg:
				ggg.append(i)
				print(ggg)
			
	return quicksort(lesser, ggg) + [pivot] + quicksort(greater, ggg)

print(quicksort([1,2,3,4], []))

def distinct(arr):
	sett = dict()
	for i in arr:
		sett[i] = 1
	return len(list(sett.keys()))

print(distinct([2,3,4,2,3,4,5,6]))

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()
	
	greater = []
	lesser = []
	
	for i in arr:
		if i > pivot:
			greater.append(i)
		else:
			lesser.append(i)
	return quicksort(lesser) + [pivot] + quicksort(greater)

gf = quicksort([2,3,1,2,3,2,4])

print(max(gf[-1] * gf[-2] * gf[-3], gf[0] * gf[1] * gf[-1]))


def triangle(arr):
		ls = [r for r in range(len(arr))]
		ls.reverse()
		i = 0
		for r in ls:
			for q in ls[i +1:]:
				for p in arr[i + 2:]:
					if arr[p] + arr[q] > arr[r] and arr[q] + arr[r] > arr[p] and arr[r] + arr[p] > arr[q]:
						return True
			i +=1
		return False

print(triangle([2,3,4,5,6,7,8,9,5]))

def triangle(arr):
	arr.sort()
	print(arr)
	ls = [r for r in range(len(arr))]
	ls.reverse()
	i = 0
	
	for r in ls:
		for q in ls[i + 1:]:
			for p in ls[i + 2:]:
				if arr[p] + arr[q] > arr[r] and arr[q] + arr[r] > arr[p] and arr[r] + arr[p] > arr[q]:
					print(r,q,p)
					return True
		i += 1
	return False

print(triangle([2,3,4,5,6,7,8,9,5]))

def triangle(A):

    #edge case check
    if len(A) < 3:
        return 0

    A.sort()
    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0


def triangle(arr):
	if len(arr) <= 2:
		return 0
	
	for i in range(len(arr)-2):
		if arr[i] + arr[i + 1] > arr[i + 2]:
			return 1
	
	return 0

ls = [2,3,4,5,6,7,8]
ls = [0] * len(ls)
print(ls)




print(triangle([2,3,4,5,6,7,8,9,5]))