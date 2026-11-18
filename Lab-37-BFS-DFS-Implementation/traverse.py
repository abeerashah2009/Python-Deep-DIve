# Adjacency list representation of a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

from collections import deque

def bfs(start_node, graph):
    visited = set()
    queue = deque([start_node])  # Initialize queue with start node

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=' ')  # Visit the node
            visited.add(node)
            queue.extend([n for n in graph[node] if n not in visited])
    print()

def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)


if __name__ == '__main__':
    print('BFS order:', end=' ')
    bfs('A', graph)
    print('DFS order:', end=' ')
    dfs('A', graph)
    print()
