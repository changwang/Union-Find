#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Nov 8, 2009

@author: changwang
'''
import unionfind1
import unionfind2
import unionfind3
import unionfind4

from utils import parser, convert

import sys
import time
import cProfile

def test(alg_num, data_set):
    if alg_num == 1:
        uf = unionfind1.UnionFind()
    elif alg_num == 2:
        uf = unionfind2.UnionFind()
    elif alg_num == 3:
        uf = unionfind3.UnionFind()
    elif alg_num == 4:
        uf = unionfind4.UnionFind()

    starttime = time.time()
#    import random
#    rand = 0
#    iter = 0
    for item in data_set:
#        iter += 1
#        if iter % 100 == 0:
#            rand = random.randint(1, len(uf.parents))
#            print iter
#            print '=== ' + str(uf.parents.keys()[rand]) + ' belongs to set: ' + str(uf.internalNameOfSet(uf.parents.keys()[rand].value)) + ' ==='
        result = convert(item)
        if result[0] == 'find':
            uf.find(result[1], True)
        elif result[0] == 'union':
            uf.union(result[1][0], result[1][1])
        
    endtime = time.time()
    
    uf.internalNameOfSet(1)
    
    del uf
    
    return (endtime - starttime)

result_set = parser('hw4.dat')

def test2():
    for i in range(10):
        test(4, result_set)

if __name__ == "__main__":
#    print "PLEASE ENTER THE NUMBER BELOW TO SELECT THE ALORGITHM"
#    print "1. Weighting rule with path-compression."
#    print "2. Weighting rule."
#    print "3. naive algorithm."
#    print
#    selection = int(raw_input("YOUR SELECTION IS:"))
#    
#    result_set = parser('hw4.dat')
#    time_set = []
#    if selection in [1, 2, 3]:
#        for i in range(100):
#            time_set.append(test(selection, result_set))
#    else:
#        err_msg = "MAKE SURE YOU ENTERED 1, 2 OR 3."
#        sys.exit(err_msg)
#    
#    print 'The average time is: ' + str(sum(time_set)/100)
    cProfile.run('test2()', 'main.prof')
    import pstats
    p = pstats.Stats('main.prof')
    p.sort_stats("time").print_stats()