nodes = {0 : [1], 
1 : [2], 2 : [0, 3], 3 : [2], 4 : [6], 5 : [4], 6 : [5]}

class Graph():
	def __init__(self):
		self.edges = {}
		self.visited = []
		self.marked = []

	def add_edges(self, edges):
		for i in edges:
			self.edges[i] = edges[i]

	def dfs(self, root):

		print(root)
		self.visited.append(root)


		for i in self.edges[root]:
			if i not in self.visited:
				self.dfs(i)


	def bfs(self, root):
		self.marked = []
		que = []
		que.append(root)

		while len(que) > 0:
			w = que.pop()
			print(w)
			self.marked.append(w)
			for i in self.edges[w]:
				if i not in self.marked:
					que.append(i)


graph = Graph()
graph.add_edges(nodes)
graph.dfs(2)
print("")
graph.bfs(2)