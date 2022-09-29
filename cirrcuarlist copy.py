class Node():
	def __init__(self):
		self.data = None
		self.next = None


node1 = Node().data = 1
node2 = Node().data = 2
node3 = Node().data = 3
node4 = Node().data = 4
node5 = Node().data = 5


node1.next = node2
node2.next = node2
node3.next = node4
node4.next = node5
node5.next = node2


def is_circular(head = None):
	if head is None:
		return True

	slow = head
	fast = head.next

	while slow != fast:
		slow = slow.next
		fast = fast.next.next
		if fast == head or slow == head:
			return True
		if fast == None or slow == None:
			return False

print(is_circular(node1))