#!/usr/bin/env python3

# In my opinion this is too difficult for the 'easy' level but here it is
# anyway. This is an implementation from stackoverflow.com/a/22899400 but
# modified to find the shortest path, rather than just its length.


def dijkstra(graph, node):
    tovisit = {v: 0 if v is node else float("inf") for v in graph.keys()}
    paths = {v: "" for v in graph.keys()}
    visited = {}

    while tovisit:
        node, total = min(tovisit.items(), key=lambda x: x[1])
        for neighbour, weight in graph[node].items():
            if neighbour in tovisit and tovisit[neighbour] > total + weight:
                tovisit[neighbour] = total + weight
                paths[neighbour] += node
        visited[node] = total
        del tovisit[node]

    return {node: path+node for node, path in paths.items()}


graph = {
    "A": {"B": 1, "C": 3},
    "B": {"D": 1},
    "C": {"A": 2, "B": 4, "D": 2},
    "D": {"C": 2}
}

# To get the quickest path from C->B
print(dijkstra(graph, "C")["B"])
