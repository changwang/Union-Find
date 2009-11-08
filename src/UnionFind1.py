#!/usr/local/bin/python
#--*-- encoding=utf-8 --*--

'''
Created on Oct 30, 2009

@author: changwang
'''

class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 1
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __repr__(self):
        return 'Node: ' + str(self.value)
    
    def __hash__(self):
        return hash(self.value)
    
class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def find(self, value):
        node = Node(value)
        if node not in self.parents:
            self.parents[node] = node.parent
            print 'current path is: ' + str(node)
            return node
        
        path = [node]
        root = self.parents[node]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
            
        for ancestor in path:
            self.parents[ancestor] = root
        print 'current path is: ' + str(path)
        return root
    
    def internalNameOfSet(self, value):
        root = self.find(value)
        print root.value
        
    def numberOfItemsInSubtree(self, value):
        for node in self.parents.keys():
            if node.value == value:
                print (node.rank - 1)
                return;

    def union(self, *args):
        roots = [self.find(node) for node in args]
        roots.sort(cmp=lambda x, y: cmp(x.value, y.value))
        heaviest = roots[0]
        
        for n in roots:
            if self.parents[n].rank > self.parents[heaviest].rank:
                heaviest = n
        
        for r in roots:
            if r!= heaviest:
                self.parents[heaviest].rank += self.parents[r].rank
                self.parents[r] = heaviest

if __name__ == '__main__':
    uf = UnionFind()
    uf.find(1)
    uf.find(3)
    uf.union(3, 1)
    uf.find(2)
    uf.find(4)
    uf.union(2, 4)
    uf.find(5)
    uf.find(6)
    uf.union(5, 6)
    uf.union(4, 5)
    uf.union(1, 6)
    print uf.parents