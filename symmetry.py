class node():
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None


#here is how we create the tree
def create_tree(arr):
	if len(arr) == 0:
		return

	mid = len(arr) // 2

	root = node(arr[mid])
	print(arr[mid])
	root.left = node()
	root.right = node()

	def helper(pnode, arr):
		mid = len(arr) // 2

		if len(arr) == 1:
			pnode.data = arr[0]
			print(arr[mid])
			return


		pnode.data = arr[mid]
		print(arr[mid])

		if len(arr[0:mid]) > 0:
			pnode.left = node()
			helper(pnode.left, arr[0:mid])

		if len(arr[mid + 1:]) > 0:
			pnode.right = node()
			helper(pnode.right, arr[mid + 1:])

	helper(root.left, arr[0:mid])
	helper(root.right, arr[mid + 1:])

	print("")
	return root









def level_order_traversal(root):
	que = []
	visited = []

	def helper(pnode):
		if pnode is None:
			return

		print(pnode.data)
		visited.append(pnode)

		if pnode.left not in que and pnode.left not in visited and pnode.left is not None:
			que.append(pnode.left)

		if pnode.right not in que and pnode.right not in visited and pnode.right is not None:
			que.append(pnode.right)