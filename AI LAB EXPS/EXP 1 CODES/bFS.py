def BFS(graph,start):
    visted=[]
    queue =[start]
    while queue:
        node = queue.pop(0)
        if node not in visted:
            print(node,end=" ")
            visted.append(node)
            for neighbour in graph[node]:
                if neighbour not in visted:
                    queue.append(neighbour)
graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
BFS(graph,'A')                     