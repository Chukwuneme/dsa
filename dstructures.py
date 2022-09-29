def isUnique(strin):
	arr = [i for i in strin]
	print(arr)
	arr.sort()

	for i in range(0,len(arr)):
		for b in range(0,len(arr)):
			if b != i:
				if arr[i] == arr[b]:
					return False

	return True

print(isUnique("heliyy"))


"""def isPerm(str1, str2):
	arr1 = [i for i in str1]
	arr2 = [i for i in str2]

	ls = []

	for char1 in range(len(arr1)):
		for char2 in range(len(arr2)):
			if arr1[char1] == arr2[char2]:
				del arr2[char2]
				ls.append(True)

	if len(ls) == len(str1):
		return True
	else:
		return False"""

#print(isPerm("hey", "hey"))

ls = [2,3,4,5,6,5,4,3,2,3,4,5,6,9,4,8,1,9]

def partitionAround(x, arr):
	ff = []
	if len(arr) < 2:
		return False

	count = 0
	#for i in range(0, len(arr)):
	while count < len(arr):
		if arr[count] < x:
			#y = arr.pop(i)
			ff.insert(0, arr[count])
			count += 1
		else:
			#y = arr.pop(count)
			ff.append(arr[count])
			count += 1
	return ff

print(partitionAround(4, ls))



class Node(object):
	"""docstring for Node"""
	def __init__(self, data, node = None):
		#super(Node, self).__init__()
		self.data = data
		self.nextnode = node

class LinkedLister(object):
	"""docstring for LinkedLister"""
	def __init__(self, node = None):
		#super(LinkedLister, self).__init__()
		self.head = node
		self.current = self.head

	def _print(self):
		self.current = self.head
		status = True
		while self.current != None:
			print(" {} ->".format(self.current.data), end = " ")
			if self.current.nextnode == None:
				print("None")
				break
			self.current = self.current.nextnode
		print(" ")

	def add(self, node):
		if self.head == None:
			self.head = node
			self.current = node
		else:
			self.current.nextnode = node
			if self.current.nextnode != None:
				self.current = self.current.nextnode
			self._print()

ls1  = [2,3,4]
ls2 = [5,6,7]
list1 = LinkedLister()
list2 = LinkedLister()

for i in range(len(ls1)):
	node1 = Node(ls1[i])
	node2 = Node(ls2[i])
	list1.add(node1)
	list2.add(node2)

		



