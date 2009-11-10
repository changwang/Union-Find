#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Nov 8, 2009

@author: changwang

Put some utilize function here.
'''

import re

def parser(filename=None):
    """ parse the input file into a readable format. """
    if filename == None:
        print "Please enter the file name!"
        return None;
    
    f = open(filename)
    whole = []
    try:
        for line in f:
            split_line = re.split(',\W+', line)
            split_line = split_line[0:-1]
            for s in split_line:
                whole.append(s)
    finally:
        f.close()

    return whole

def convert(str):
    """ convert the each item into the readable format. """
    result = re.findall('\d+', str)
    if str.startswith("f"):
        return ('find', int(result[0]))
    elif str.startswith("u"):
        return ('union', (int(result[0]), int(result[1])))

def path_printer(path):
    """ print the path. """
    if len(path) == 1:
        print str(path[0]) + ' currently is in its own singleton set'
        return
    
    for node in path:
        if node == path[-1]:
            print str(node)
        else:
            print str(node) + ' ➜',
