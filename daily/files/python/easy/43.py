#!/usr/bin/python3

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G", "H"],
    "F": ["I"],
    "G": [],
    "H": [],
    "I": []
}


def parent(node, tree):
    for leaf in tree.keys():
        if node in tree[leaf]:
            return leaf


def ancestors(node, tree):
    parents = [node]
    while parent(node, tree):
        parents.append(parent(node, tree))
        node = parent(node, tree)
    return parents


def lowest(a, b, tree):
    if a == b:
        return a
    common = [v for v in ancestors(a, tree) if v in ancestors(b, tree)]
    for c in common:
        for d in common:
            if parent(d, tree) == c:
                break
        return c


print(lowest("D", "G", tree))
