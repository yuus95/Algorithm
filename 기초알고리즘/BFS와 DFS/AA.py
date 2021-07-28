from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def DFS(graph,start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

def BFS(graph,start_node):
    visit = list()
    q = deque()
    q.append(start_node)

    while q:
        node = q.popleft()

        if node not in visit:
            visit.append(node)
            q.extend(graph[node])

    return visit





print(DFS(graph,'A'))

print('bfsbfs',BFS(graph,'A'))
