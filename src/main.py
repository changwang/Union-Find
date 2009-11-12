#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Nov 8, 2009

@author: changwang

Main entry of this program.
'''
import unionfind1
import unionfind2
import unionfind3

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

    starttime = time.time()
    for item in data_set:
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

def main():
    print "PLEASE ENTER THE NUMBER BELOW TO SELECT THE ALORGITHM"
    print "1. Weighting rule with path-compression."
    print "2. Weighting rule."
    print "3. Naive algorithm."
    print
    selection = int(raw_input("YOUR SELECTION IS: "))
    
    result_set = parser('hw4.dat')
    time_set = []
    if selection in [1, 2, 3]:
        for i in range(10):
        # run the algorithm 10 times, then get the average time.
            time_set.append(test(selection, result_set))
    else:
        err_msg = "MAKE SURE YOU ENTERED 1, 2 OR 3."
        sys.exit(err_msg)
    
    print 'The average time is: ' + str(sum(time_set)/len(time_set)) + ' second(s)'

if __name__ == '__main__':
    cProfile.run('main()', 'main.prof')
    import pstats
    p = pstats.Stats('main.prof')
    p.sort_stats("calls").print_stats()