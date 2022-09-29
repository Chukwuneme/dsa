d = {"A" : ["B", "C", "D"], "B" : ["C", "D", "A"]}




class Graph():
	def __init__(self, nodes = []):
		self.nodes = nodes
		self.edges = {}
		self.visited = []

	def add_edges(self, data = {}):
		for a in data:
			self.edges[a] = data[a]
		return self.edges

	def print_edges(self):
		for a in self.edges:
			print(a, " -> ", self.edges[a])

	def dfs(self, node):
		print(node)
		self.visited.append(node)

		"""if self.edges.get(node) is None:
			print("Value {} not a start node in graph".format(node))
			return"""


		#def ddfs(node1):

		"""w = stack.pop()

			if w in visited:
				if len(stack) > 0:
					w = stack.pop()
					ddfs(w)
				return

			print(w)
			visited.append(w)"""

		"""if self.edges.get(node1) is None:
				if len(stack) > 0:
					w = stack.pop()
					ddfs(w)
				else:
					return"""


		if self.edges.get(node) is not None:
			for edge in self.edges[node]:
				if edge not in self.visited:
					self.dfs(edge)

		"""if len(stack) > 0:
			w = stack.pop()
			ddfs(w)

		ddfs(node)"""


	def bfs(self, node):
		pass



graph = Graph()
graph.add_edges(d)
graph.print_edges()
graph.dfs("A")

