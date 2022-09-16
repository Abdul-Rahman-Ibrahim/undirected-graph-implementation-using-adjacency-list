#implementing of an undirected graph using adjacency list

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            
class Graph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
        
    def add_edge(self, u, v):
        self.vertices[u].add_neighbor(v)
        self.vertices[v].add_neighbor(u)
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
            
g = Graph()
g.add_vertex(Vertex("A"))
g.add_vertex(Vertex("B"))
g.add_vertex(Vertex("C"))
for i in range(ord("A"), ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

    
