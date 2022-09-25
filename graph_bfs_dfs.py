#undirected graph implementation using adjacency list

class Vertex:
    def __init__(self,name):
        self.name = name
        self.neigbors = []
        

class Graph:
    vertices = {}
    
    def add_vertex(self,v):
        if isinstance(v,Vertex) and v not in self.vertices:
            self.vertices[v.name] = v

    def add_edge(self,v,u):
        if u not in self.vertices[v].neigbors:
            self.vertices[v].neigbors.append(u)

        if v not in self.vertices[u].neigbors:
            self.vertices[u].neigbors.append(v)

    def bfs(self,s):
        self.visited = {}
        self.distance = {}
        self.parent = {}
        q = []
        #initialize
        for v in self.vertices:
            self.visited[v] = False
            self.distance[v] = -1
            self.parent[v] = None

        #mark the source node(s) as visited and enqueue it
        self.visited[s] = True
        self.distance[s] = 0
        q.append(s)
        graph_str = ""
        while q:
            s = q.pop(0)
            graph_str += s+"-->"
            #traverse through the neigbors of source and mark
            #adjacent neigbors as visited
            for neigbor in self.vertices[s].neigbors:
                if not self.visited[neigbor]:
                    self.visited[neigbor] = True
                    self.parent[neigbor] = s
                    self.distance[neigbor] = self.distance[s]+1
                    q.append(neigbor)
        print(graph_str[:-3])

    def dfs(self):
        self.graph_str = ""
        self.time = 0
        self.color = {} #W G B
        self.parent = {}
        self.trav_time = {} #[start,end]
        #initialize
        for v in self.vertices:
            self.color[v] = "W"
            self.parent[v] = None
            self.trav_time[v] = [-1,-1]
            
    def dfs_util(self,s):
        self.color[s] = "G"
        self.trav_time[s][0] = self.time
        self.time += 1
        self.graph_str += s+"-->"
        for neigbor in self.vertices[s].neigbors:
            if self.color[neigbor] == "W":
                self.parent[neigbor] = s
                self.dfs_util(neigbor)
                
        self.color[s] = "B"
        self.trav_time[s][1] = self.time
        self.time += 1
        
    def print_graph(self):
        for vertex in self.vertices:
            print(vertex,"-->",self.vertices[vertex].neigbors)

if __name__=="__main__":
    g = Graph()
    for i in range(ord("A"), ord("K")):
        g.add_vertex(Vertex(chr(i)))
    edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])
    print("Graph using adjacency list")
    g.print_graph()
    print("\n")

    #######BFS
    s = "A"
    print("Breadth first search from source vertex {0}".format(s))
    g.bfs(s)
    print("\n")
    ##shortest distance of all vertex from source vertex
    print("Shortest distance of all vertex from vertex {0}".format(s))
    print(g.distance)
    print("\n")
    ##shortes path of source vertex from any vertex
    v = "G"
    start = "G"
    path = ""
    while v is not None:
        path += v+"-->"
        v = g.parent[v]
    path = path[:-3]
    print("Shortest path from vertex {0} to vertex {1}".format(start,s))
    print(path)
    print("\n")

    #######DFS
    g.dfs()
    #using for loop for dfs ensures that vertex that
    #aren't connected are also traversed.
    for s in g.vertices.keys():
        if g.color[s] == "W":
            g.dfs_util(s)
    print("Depth first search".upper())
    print(g.graph_str[:-3])
    print("\n")
    print("Travel time of depth first search")
    print(g.trav_time)
