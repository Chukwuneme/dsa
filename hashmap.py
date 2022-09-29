class hashmap():
	def __init__(self):
		self.size = 64
		self.map = [None] * self.size
		print(self.map)
	
	def _hasher(self, key):
		hash = 0
		for char in str(key):
			hash += ord(str(char))
		return hash % self.size

	def add(self, key, val):
		data = [key, val]
		index = self._hasher(key)
		if self.map[index] == None:
			print("added key {} and value {}".format(key, val))
			self.map[index] = [data]
			print(self.map)
			return True
		else:
			for pair in self.map[index]:
				if pair[0] == key:
					pair[1] = val
					print("added key {} and value {}".format(pair[0], pair[1]))
					return True
			self.map[index].append(data)
			print("added key {} and value {}".format(key, val))
			return True
			
	def get(self, key):
		index = self._hasher(key)
		if self.map[index] == None:
			return False
		for pair in self.map[index]:
			if pair[0] == key:
				return pair[1]
		return None
	
	def pop(self, key):
			index = self._hasher(key)
			for i in range(len(self.map[index])):
				if self.map[index][i][0] == key:
					self.map[index].pop(i)
					return True
			return False
mm = hashmap()
mm.add("a", 2)
mm.add("d", 3)
print(mm.get("a"))
print(mm.pop("a"))
print(mm.get("a"))