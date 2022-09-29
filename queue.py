array = [3,4,5,6,7]

class queue():
	def __init__(self):
		self.data = []
		self.size = len(self.data)
	
	def pop(self):
		if self.size == 0:
			print("cant delete from empty queue")
			return
		v = self.data[-1]
		del self.data[-1]
		self.size -= 1
		return v
	
	def push(self, val):
		self.data.append(val)
		self.size += 1
		print("appended {}".format(val))

li = queue()
li.pop()
		