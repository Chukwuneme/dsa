ls = [2,3,4,6,3,2,4,3]

class stack():
	def __init__(self):
		self.data = []
		self.size = len(self.data)
	
	def push(self, data):
		self.data.append(data)
		self.size += 1
		print("appended {} to stack".format(data))
		
	def pop(self):
		v = self.data[-1]
		del self.data[-1]
		self.size -= 1
		print("removed value from stack")
		return v

stac = stack()
for i in ls:
	stac.push(i)

rr = stac.pop()
print(stac.size)