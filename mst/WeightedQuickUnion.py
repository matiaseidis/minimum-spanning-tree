'''
Created on 28/6/2015

@author: matiaseidis
'''

class UnionFind:
    
    def __init__(self, size):
        self.size = size
        self.components = [i for i in range(0, size)]
        self.tree_sizes = [1] * size
        
    def connect(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        if(a_root is not b_root): 
            if(self.tree_sizes[a_root] < self.tree_sizes[b_root]):
                self.components[a_root] = b_root
                self.tree_sizes[b_root] += self.tree_sizes[a_root]
            else: 
                self.components[b_root] = a_root
                self.tree_sizes[a_root] += self.tree_sizes[b_root]
       
    def connected(self, a, b):
        return self.root(a) is self.root(b)
    
    def root(self, a):
        while a is not self.components[a]:
            # path compression optimization
            self.components[a] = self.components[self.components[a]] 
            a = self.components[a]
        return a
    
# short test
# uf = UnionFind(3)
# print(uf.connected(0, 1))
# print(uf.connected(0, 2))
# uf.connect(0, 2)
# print(uf.connected(0, 1))
# print(uf.connected(0, 2))

        
            