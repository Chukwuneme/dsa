class node():
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None





class binarySearch(object):
	"""docstring for ClassName"""
	def __init__(self, head = None):
		self.head = head
		self.current = None


	def createtree(self, arr, noder = None):
		arr.sort()
		if noder == None:
			nodes = self.head
		else:
			nodes = noder

		if len(arr) > 0:
			mid = len(arr) // 2
			print(mid)
			node1 = node(arr[mid])
			if nodes == None:
				print("")
				self.head = node1
				nodes = node1
				nodes.right = self.createtree(arr[mid:], nodes)
				nodes.left = self.createtree(arr[0:mid], nodes)
				

			else:
				print("ccccccccccc")
				if mid > nodes.data:
					if nodes is None:
						nodes = node1 
						nodes = nodes.right
						self.createtree(arr[mid:], nodes)
					else:
						nodes = nodes.right
						self.createtree(arr[mid:], nodes)
				elif mid < nodes.data:
					if nodes.left is None:
						nodes.left = node1 
						nodes = nodes.left
						self.createtree(arr[0:mid], nodes)
					else:
						nodes = nodes.left
						self.createtree(arr[0:mid], nodes)

		else:
			print("empty array")

	


	def printer(self):
		print("fff")

		node1 = self.head

		def gg(node):
			if node is None:
				return

			gg(node.left)
			print(node.data)
			gg(node.right)

		gg(node1)


def fibonacci(i):
	if i == 0:
		return 0
	if i == 1:
		return 1
	return fibonacci(i - 1) + fibonacci(i - 2)


def createtree2(arr):
		if len(arr) <= 0:
			return None

		mid = len(arr) // 2

		nod = node(arr[mid])


		nod.left = createtree2(arr[0:mid])
		nod.right = createtree2(arr[mid + 1:])

		print(arr[mid])

		return nod


dd = [1,2,3,4,5,6,7,8,9,10]
tree = binarySearch()
de = createtree2(dd)

print("")

def gg(node):
	if node is None:
		return

	gg(node.left)
	print(node.data)
	gg(node.right)
gg(de)


tree.printer()
print(fibonacci(10))



		