# graphs

Graphs are a data structure used to represent a visual of relationships between data vertices (the Nodes of a graph). The links that connect vertices together are called edges.
Edges define which vertices are connected but do not indicate a direction flow between them. Each vertex has connections to other vertices which are saved on the vertex as a comma-separated list.

There are also special graphs called directed graphs that define a direction of the relationship, similar to a linked list. Directed graphs are helpful when modeling one-way relationships or a flowchart-like structure.


They’re primarily used to convey visual web-structure networks in code form. These structures can model many different types of relationships like hierarchies, branching structures, or simply be an unordered relational web. The versatility and intuitiveness of graphs makes them a favorite for data science.
When written in plain text, graphs have a list of vertices and edges:
V = {a, b, c, d, e}
E = {ab, ac, bd, cd, de}
In Python, graphs are best implemented using a dictionary with the name of each vertex as a key and the edges list as the values.

# Create the dictionary with graph elements
graph = { "a" : ["b","c"],
                 "b" : ["a", "d"],
                 "c" : ["a", "d"],
                  "d" : ["e"],
                  "e" : ["d"]
         }
# Print the graph          
print(graph)

Advantages:
Quickly convey visual information through code
Usable for modeling a wide range of real-world problems
Simple to learn the syntax
Disadvantages:
Vertex links are difficult to understand in large graphs
Time expensive to parse data from a graph
Applications:
Excellent for modeling networks or web-like structures
Used to model social network sites like Facebook
Common graph interview questions in Python
Detect cycle in a directed graph
Find a “Mother Vertex” in a directed graph
Count the number of edges in an undirected graph
Check if a path exists between two vertices
Find the shortest path between two vertices
