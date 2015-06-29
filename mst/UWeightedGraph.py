'''
Created on 28/6/2015

@author: matiaseidis
'''

class UWeightedGraph:
    
    def __init__(self):
        self.edges = []
        self.v = set()
        
    def add_edge(self, v, w, weight):
        self.edges.append((v,w,weight))
        self.v.add(v)
        self.v.add(w)
        
    def E(self):
        return self.edges
     
    def V(self):
        return self.v
            
