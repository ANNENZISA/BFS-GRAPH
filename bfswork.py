# Python Program to print BFS transversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,a,b):
		self.graph[a].append(b)

	# Function to print a BFS of graph
	def BFS(self, c):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(c)
		visited[c] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			c = queue.pop(0)
			print (c, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex c. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for c in self.graph[c]:
				if visited[c] == False:
					queue.append(c)
					visited[c] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 1)
g.addEdge(3, 4)
g.addEdge(5, 5)

print ("BFS Traversal"
				" (starting from vertex 3)")
g.BFS(3)

