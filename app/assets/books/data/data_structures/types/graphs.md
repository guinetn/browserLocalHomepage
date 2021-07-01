# Graphs

Math structures that outlines the relationships between elements

- Nodes (the numbered dots at the edges of the decagon below)
- Edges (the lines that connect the nodes: their relationship)

Perfect graph: a graph with all its nodes connected

## Graph search algorithms
Common - Breadth-first Search, Depth-first Search
Uncommon - Topological Sort, Dijkstra's algorithm
Rare - Bellman-Ford algorithm, Floyd-Warshall algorithm, Prim's algorithm, Kruskal's algorithm


Usually defined as 2-D matrices where cells are the nodes and each cell can traverse to its adjacent cells (up/down/left/right). 
Traversing a 2-D matrix: ensure your current position is within the boundary of the matrix and has not been visited before.

Depth-first searches on a matrix:

```python
def dfs(matrix):
  # Check for an empty graph
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    if (i, j) in visited:
      return

    visited.add((i, j))
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        # Add in your question-specific checks.
        traverse(next_i, next_j)

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)
```

Breadth-first searches on the matrix:

```python
from collections import deque

def bfs(matrix):
  # Check for an empty graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited:
        visited.add((curr_i, curr_j))
        # Traverse neighbors.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols:
            # Add in your question-specific checks.
            queue.append((next_i, next_j))

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)
```      
      
### more

- https://pub.towardsai.net/graph-theory-creating-a-relationship-network-in-python-f7b6ecf7f50      