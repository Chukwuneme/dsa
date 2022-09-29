array = [2,4,6,4,7,9,4,7,2,5]
sorted_array = [2,3,4,5,6,7,8,9]

class LinkedListNode():
	def __init__(self, data, node = None):
		self.data = data
		self.next = node

class LinkedList():
	def __init__(self, node = None):
		self.head = node
		self.current = self.head
		if self.head == None:
			print("Empty list created")
		else:
			print("Head node created with value {}".format(self.head.data))
	
	def append(self, node):
		if self.head == None:
			self.head == node
			print("Head node created with value {}".format(self.head.data))
		else:
			self.current.next = node
			self.current = node
			print("Node created with value {}".format(self.current.data))

node = LinkedListNode(3)

arr = LinkedList(node)
for i in array:
	node = LinkedListNode(i)
	arr.append(node)

		
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

