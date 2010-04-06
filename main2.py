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
import unionfind5
import unionfind6

from utils import parser, convert

import sys
import time
import cProfile

def test(alg_num, data_sets):
    if alg_num == 1:
        uf = unionfind1.UnionFind()
    elif alg_num == 2:
        uf = unionfind2.UnionFind()
    elif alg_num == 3:
        uf = unionfind3.UnionFind()
    elif alg_num == 4:
        uf = unionfind4.UnionFind()
    elif alg_num == 5:
        uf = unionfind5.UnionFind()
    elif alg_num == 6:
        uf = unionfind5.UnionFind()

    time_set = []
    data_sets = data_sets * 100
    for date_set in data_sets:
        starttime = time.time()
        for item in date_set:
            result = convert(item)
            if result[0] == 'find':
                uf.find(result[1], True)
            elif result[0] == 'union':
                uf.union(result[1][0], result[1][1])
            
        endtime = time.time()
        
        time_set.append(endtime - starttime)
    
    del uf
    
    return time_set

data_sets = []
data_sets.append(parser('1.dat'))
data_sets.append(parser('2.dat'))
data_sets.append(parser('3.dat'))
data_sets.append(parser('4.dat'))
data_sets.append(parser('5.dat'))
data_sets.append(parser('6.dat'))
data_sets.append(parser('7.dat'))


def test2():
    result = test(4, data_sets)

if __name__ == "__main__":
    cProfile.run('test2()', 'main.prof')
    import pstats
    p = pstats.Stats('main.prof')
    p.sort_stats("calls").print_stats()