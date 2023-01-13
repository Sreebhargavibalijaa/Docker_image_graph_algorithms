from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        final_nodes = []
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            final_nodes.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return final_nodes

    def DFSUtil(self, v, visited, final_nodes):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        final_nodes.append(v)
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, final_nodes)
              
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited,final_nodes)
        return final_nodes
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
final_nodes = []
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
print(g.BFS(2))
print("Following is Depth First Traversal"
      " (starting from vertex 2)")
print(g.DFS(2))