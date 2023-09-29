# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def hamiltonianPaths(graph, v, visited, path, n):
 
    # if all the vertices are visited, then the Hamiltonian path exists
    if len(path) == n:
        # print the Hamiltonian path
        print(path)
        return
 
    # Check if every edge starting from vertex `v` leads to a solution or not
    for w in graph.adjList[v]:
 
        # process only unvisited vertices as the Hamiltonian
        # path visit each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)
 
            # check if adding vertex `w` to the path leads to the solution or not
            hamiltonianPaths(graph, w, visited, path, n)
 
            # backtrack
            visited[w] = False
            path.pop()
 
 
def findHamiltonianPaths(graph, n):
 
    # start with every node
    for start in range(n):
 
        # add starting node to the path
        path = [start]
    
        # mark the start node as visited
        visited = [False] * n
        visited[start] = True
    
        hamiltonianPaths(graph, start, visited, path, n)
 
 
if __name__ == '__main__':
 
    # consider a complete graph having 4 vertices
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
 
    # total number of nodes in the graph (labelled from 0 to 3)
    n = 4
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    findHamiltonianPaths(graph, n)