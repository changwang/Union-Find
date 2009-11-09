'''
Created on Nov 8, 2009

@author: changwang

Define some data structures that could be used by other data structure.
'''

class Node:
    ''' The node class represents the node in the disjoint set and union-find tree. '''
    
    def __init__(self, value):
        ''' construct function. '''
        
        # The parent node of current node, at first each node points to itself.
        self.parent = self
        
        # The data is contained in the node.
        self.value = value
        
        # The rank means how many nodes are contained by current node. 
        self.rank = 1
    
    def __eq__(self, other):
        ''' This method is used to handle whether two nodes are equal,
        like node1 == node2.
        Actually, if the value in node is the same, two nodes are the same. '''
        return self.value == other.value
    
    def __ne__(self, other):
        ''' This method is used to handle wheter two nodes are not equal,
        like node1 != node2 or node1 <> node2.
        Acutally, if the value in node is not the same, two nodes are different. '''
        return self.value != other.value
    
    def __repr__(self):
        ''' This method is used to help debug, 
        which give the console a readable information. '''
        return 'Node: ' + str(self.value)
    
    def __hash__(self):
        ''' The node should be hashable,
        due to the dictionary requirement. '''
        return hash(self.value)