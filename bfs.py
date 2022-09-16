#getting sample adjacency graph from a file
from graph import Graph
graph = Graph().vertices
adj_lst = {}
for vertex in graph:
    adj_lst[vertex] = graph[vertex].neighbors

#breadth first search 
from queue import Queue
visited = {}
distance = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in graph:
    visited[node] = False
    parent[node] = None
    distance[node] = -1

s = "A"
visited[s] = True
distance[s] = 0
queue.put(s)
while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in adj_lst[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            distance[v] = distance[u] + 1
            queue.put(v)

print(bfs_traversal_output)
print(distance)
