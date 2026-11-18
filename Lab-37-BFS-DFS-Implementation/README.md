# Lab 37 – BFS and DFS Implementation

## 1. Lab Overview

**Topic:** Breadth-First Search (BFS) and Depth-First Search (DFS)
**Language:** Python 3.12.3
**Platform:** Ubuntu 24.04
**Libraries:** Python Standard Library
**LMS Result:** 100/100 – Passed

## 2. Learning Objectives

In this lab, I learned how to:

- Represent a graph using an adjacency list.
- Implement Breadth-First Search (BFS).
- Implement Depth-First Search (DFS) using recursion.
- Use queues and sets in graph traversal.
- Understand the difference between BFS and DFS.

## 3. What Is a Graph?

A graph is a data structure consisting of:

- **Vertices (Nodes):** Individual elements in a graph.
- **Edges:** Connections between nodes.

Graphs are used in computer networks, maps, social networks, and navigation systems.

## 4. Adjacency List Representation

An adjacency list stores each node with a list of its neighboring nodes.

Example:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

In this graph:

- A connects to B and C.
- B connects to D and E.
- C connects to F.
- D and F have no outgoing connections.
- E connects to F.

## 5. Breadth-First Search (BFS)

BFS explores a graph level by level.

It uses a queue to process nodes in the order they are discovered.

### Important concepts

- `deque`: Provides an efficient queue.
- `popleft()`: Removes the first item from the queue.
- `visited`: Keeps track of visited nodes.
- `extend()`: Adds neighboring nodes to the queue.

### BFS implementation

```python
from collections import deque

def bfs(start_node, graph):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend([n for n in graph[node] if n not in visited])

    print()
```

### BFS output

```text
A B C D E F
```

### Applications of BFS

- Finding shortest paths in unweighted graphs.
- Exploring network connections.
- Level-order traversal.
- Finding nearby nodes.

## 6. Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking.

This implementation uses recursion.

### Important concepts

- `visited`: Prevents repeated node visits.
- `dfs()`: Calls itself to explore neighboring nodes.
- **Recursion:** A function calling itself.
- **Backtracking:** Returning to an earlier node when a path ends.

### DFS implementation

```python
def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)
```

### DFS output

```text
A B D E F C
```

### Applications of DFS

- Graph exploration.
- Cycle detection.
- Backtracking problems.
- Maze and puzzle solving.

## 7. BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Full name | Breadth-First Search | Depth-First Search |
| Approach | Level by level | Deep path first |
| Data structure | Queue | Recursion / Stack |
| Memory | Can store many frontier nodes | Stores current traversal path |
| Shortest path | Yes, in unweighted graphs | Not guaranteed |
| Common uses | Shortest paths | Backtracking and exploration |

## 8. Time and Space Complexity

For a graph represented by an adjacency list:

- **BFS Time Complexity:** O(V + E)
- **DFS Time Complexity:** O(V + E)

Where:

- V = Number of vertices (nodes).
- E = Number of edges.

Both algorithms can require O(V) additional space for visited tracking and traversal storage.

## 9. Complete Program

The complete executable program is saved in:

`traverse.py`

Run it with:

```bash
python3 traverse.py
```

Expected output:

```text
BFS order: A B C D E F
DFS order: A B D E F C
```

## 10. Verification

The following checks were completed:

- Python version: 3.12.3
- Graph nodes: 6
- BFS output: Correct
- DFS output: Correct
- Python syntax check: PASS
- Python recursion limit: 1000

Detailed terminal output is saved in:

`evidence/verification.txt`

## 11. Conclusion

In this lab, I successfully implemented BFS and DFS using Python.

I learned how adjacency lists represent graph connections, how BFS uses a queue to explore nodes level by level, and how DFS uses recursion to explore deeply before backtracking.

Both algorithms are important for solving graph-related problems in software development, networking, and computer science.

## 12. LMS Assessment Result

**Final Score: 100/100**

**Status: PASSED**

The practical was successfully evaluated by Al Baari.
