'''
Created on 28/6/2015

@author: matiaseidis
'''
from mst.UWeightedGraph import UWeightedGraph
from mst.UnionFind import UnionFind

def minimum_spanning_tree(tree):

    result = []
    uf = UnionFind(len(tree.V())+1)
    edges = sorted(tree.E(), key=byWeight)

    while edges:

        minor_edge = edges[0]
        edges.remove(minor_edge)
        v = minor_edge[0]
        w = minor_edge[1]
        if not uf.connected(v, w):
            result.append(minor_edge)
            uf.connect(v, w)

    return result

def byWeight(edge):
    return edge[2]

    
g = UWeightedGraph()
g.add_edge(1,10,9)
g.add_edge(1,3,3)
g.add_edge(1,2,6)
g.add_edge(3,10,9)
g.add_edge(3,2,4)
g.add_edge(10,9,8)
g.add_edge(10,8,18)
g.add_edge(9,3,9)
g.add_edge(9,4,8)
g.add_edge(3,4,2)
g.add_edge(4,2,2)
g.add_edge(4,5,9)
g.add_edge(2,5,9)
g.add_edge(9,5,7)
g.add_edge(9,8,10)
g.add_edge(9,7,9)
g.add_edge(7,8,3)
g.add_edge(6,8,4)
g.add_edge(7,6,1)
g.add_edge(5,6,4)
g.add_edge(5,7,5)
print(minimum_spanning_tree(g))

