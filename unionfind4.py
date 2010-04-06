#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    ''' 
    The Union-Find data structure.
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
        self.weights = {}
    
    def find(self, value, print_path=False):
        
        if value not in self.parents:
            ''' If the given value is not in the tree yet,
            then create it.'''
            
            self.parents[value] = value
            self.weights[value] = 1
            return value
        
        ''' This is a critical part in this method.
        from the given node, travelling back to its ancestor.
        '''
        path = [value]
        root = self.parents[value]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
            
        ''' This part handles the path-compression,
        changing the parent of the nodes which are in the path to root .'''
        for ancestor in path:
            self.parents[ancestor] = root
        
        return root

    def union(self, *values):
        ''' merge the sets which contain the given values. '''
        
        roots = [self.find(x) for x in values]
        roots.sort()
        if len(roots) <= 1:
            ''' If the length of the list is less or equal than 1,
            which means the given nodes are in the same set. '''
#            print 'The node ' + str(values[0]) + ' and node ' + str(values[1]) + ' are in the same set.'
            return
        
        # here I sort the list, because I wanna handle the items by ascending order.
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        
        for n in roots:
            if n != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
