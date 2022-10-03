class Node():
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None

	def append(self, val):
		node = Node(val)
		if not self.head:
			self.head = node
			print("added val {} to list".format(val))

		else:
			end = self.head
			while end.next:
				end = end.next

			end.next = node
			print("added val {} to list".format(val))

	def print_list(self):
		current = self.head
		while current:
			print(current.val)
			current = current.next

	def delete(self, val):
		prev = None
		current = self.head
		if not self.head:
			print("empty list can't delete anything")
			return
		elif self.head.val == val:
			self.head = self.head.next
			print("value {} deleted".format(val))
			return

		while current and current.val != val:
			prev = current
			current = current.next
		if current is None:
			print("Value not in list")
			return
		else:
			if current.val == val:
				prev.next = current.next
				print("value {} deleted".format(val))
				return

		print("value not present in list")



	def insert_at_head(self, val):
		node = Node(val)

		if not self.head:
			self.head = node
			print("added value {} to head".format(val))
		else:
			node.next = self.head
			self.head = node
			print("added value {} to head".format(val))



	def insert_in_between(self, prev, val):
		node = Node(val)
		current = self.head
		while current:
			if current.val == prev:
				node.next = current.next
				current.next = node
				print("inserted value {0} after {1} ".format(val, current.val))
				return
			current = current.next
		
		print("cant find position to insert value")
		return


			

nums  = [1,2,3,4,5,6,7]
llist = LinkedList()


for a in nums:
	llist.append(a)

llist.insert_in_between(5, 7)
llist.insert_in_between(5, 7)
llist.insert_in_between(0, 7)
llist.insert_at_head(7)
llist.print_list()
llist.delete(5)
llist.print_list()
llist.delete(7)
llist.print_list()
llist.delete(7)
llist.print_list()



