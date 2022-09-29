
#lets define our node class
class Node():
	def __init__(self):
		self.data = None
		self.next = None


#initialize individual nodes
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()



#join the nodes together to make a linked list
node1.next = node2
node3.next = node4
node4.next = node5
node5.next = node2


#lets create the check if our list is circular
def is_circular(head = None):
	if head is None:
		return False

	slow = head
	fast = head.next

	while slow != None and fast != None and fast.next != None:
		
		if fast == slow:
			return True

		slow = slow.next
		fast = fast.next.next

	return True

#check if the linked list is circular
print(is_circular(node1))