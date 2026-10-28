def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ")

print("Graph:", graph)
print("DFS Traversal:", end=" ")

visited = set()
dfs(graph, start, visited)
print()