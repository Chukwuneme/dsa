ls = [2,3,4,5,3,3,5,1,4,3]

class treenode():
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class tree():
	def __init__(self, root = None):
		self.root = root
		self.current = self.root
	
	def insert(self, node):
		if self.root == None:
			self.root == node
			self.current = node


end = len(ls)
begin = 0
mid = begin + (end - begin) // 2

def createtree(arr):
	if not arr:
		return None
	mid = len(arr) // 2
	node = treenode(arr[mid])
	print(node.data)
	node.left = createtree(arr[0:mid])
	node.right = createtree(arr[mid+1:])
	return node

treed = createtree(ls)

def search(root, key):
	if root == None or root.data == key:
		return root
	
	if root.data < key:
		return search(root.right, key)

	return search(root.left, key)

fff = search(treed, 2)
print(fff.data)
		