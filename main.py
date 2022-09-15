import sys
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def printTree(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
    def min_Key(self, key, mstSet): 
        min = 9999999 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
    def prim(self): 
        key = [9999999] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 
  
        for cout in range(self.V):  
            u = self.min_Key(key, mstSet)  
            mstSet[u] = True
            for v in range(self.V):  
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printTree(parent) 
  
g = Graph(5) 
g.graph = [ [0, 0, 4, 0, 0], 
            [0, 0, 5, 3, 0], 
            [4, 5, 0, 0, 0], 
            [0, 3, 0, 0, 2], 
            [0, 0, 0, 2, 0]] 
  
g.prim(); 