with open('rosalind_tree (1).txt', 'r') as tree:
    edges = [tuple(map(int, line.split())) for line in tree.readlines()]
n = edges.pop(0)[0]
min_edges= (n-1)-len(edges)
print(min_edges)