#!/usr/local/bin/python
#--*-- encoding=utf-8 --*--

'''
Created on Oct 30, 2009

@author: changwang

Solution 1 to union-find structure.
In this solution, using weighting rule and path-compression.
the time of this algorithm should be O(nG(n)).
G(n) is inverse of Ackermann's function.
So, the time could be considered linear time.
'''

from datastructure import Node

class UnionFind:
    ''' The Union-Find data structure.
    Each UnionFind instance maintains a family of disjoint sets of
    hashable objects, supporting the following methods:
    
    - find(value) returns a node for the set containing the given value.
    Each set is named by the smallest item in the set;
    as long as the set remains unchanged it will keep the same name.
    If the item is not yet part of a set in UnionFind, a new singleton set
    is created for it.
    
    - union(value1, value2) merges the sets containing each item into
    a single larger set. If any item is not yet part of a set in UnionFind,
    it is added to UnionFind as one of the members of the merged set.
    
    - internalNameOfSet(value) returns the name of the set containg the
    given value.
    
    - numberOfItemsInSubtree(value) returns the number of items 
    in the subtree rooted at the node which contains the given value.
    '''
    
    def __init__(self):
        ''' create a new empty union find tree. '''
        # In this dictionary, I use node as the key,
        # the parent node as the value.
        self.parents = {}
    
    def find(self, value):
        node = Node(value)
        
        if node not in self.parents:
            ''' If the given value is not in the tree yet,
            then create it.'''
            
            self.parents[node] = node.parent
            print 'current path is: ' + str(node)
            return node
        
        ''' This is a critical part in this method.
        from the given node, travelling back to its ancestor.
        '''
        path = [node]
        root = self.parents[node]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
            
        ''' This part handles the path-compression,
        changing the parent of the nodes which are in the path to root .'''
        for ancestor in path:
            self.parents[ancestor] = root
        
        print 'current path is: ' + str(path)
        # return the root of the set
        return root
    
    def internalNameOfSet(self, value):
        ''' Find the root of the set, then return its name. '''
        root = self.find(value)
        print root.value
        
    def numberOfItemsInSubtree(self, value):
        ''' Find the node, then return number of items in the subtree. '''
        for node in self.parents.keys():
            if node.value == value:
                print (node.rank - 1)
                return;

    def union(self, *args):
        #roots = [self.find(node) for node in args]
        roots = []
        for value in args:
            if self.find(value) not in roots:
                roots.append(self.find(value))
        if len(roots) <= 1:
            print 'The node ' + str(args[0]) + ' and node ' + str(args[1]) + ' are in the same set.'
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
    uf.union(3, 1, 5)
    print uf.parents
