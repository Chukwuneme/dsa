class Node(object):
	"""docstring for ClassName"""
	def __init__(self, data):
		self.data = data
		self.next = None


def reverse_list(ls):
	left = None
	middle = ls
	right = middle.next
	end = True

	while end:
		
		print(middle.data)
		middle.next = left
		if right == None:
			break
		left = middle
		middle = right
		right = right.next
	print("")
		

	while middle != None:
		print(middle.data)
		middle = middle.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

reverse_list(n1)



		