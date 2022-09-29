class Node(object):
	"""docstring for ClassName"""
	def __init__(self, data):
		self.data = data
		self.next = None


def find_nth_node(ls, k):
	i = 1
	val = None
	cur = ls
	se = False

	while True:
		if i == k:
			val = ls
			se = True

		cur = cur.next
		i += 1
		if se:
			val = val.next
			if cur.next == None:
				break
	print(val.data)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

find_nth_node(n1, 4)